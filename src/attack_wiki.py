import re, csv, json
import sys, os
import wikipediaapi
sys.path.append('..')

import utility.model as model_utils
import base_prompt
import base_prompt as bp
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from defense_utils import Defender

import random
from colorama import Fore
from copy import deepcopy
import src.safe_eval as safety_eval
import logging
logger = logging.getLogger()


def random_choose(N, seed=64):

    with open('./data/comendatory_terms-manually.json', 'r') as fp:
        data = json.load(fp)
    
    comendatory_words = [element for category in data['categories'] for k, v in category['subcategories'].items() for element in v.split(', ')]
    comendatory_words = list(set(comendatory_words))
    # print(f'The length of commendatory words is : {len(comendatory_words)}')    
            
    random_selection = random.sample(comendatory_words, N)   
    return random_selection


def ins_paraphrase(instruction):
    
    def need_paraphrase(instruction):
        ...
        return True
    
    def ins_paraphrase_helper(instruction):
        ...
        return instruction
    
    GPP_instance = base_prompt.GPTParaPrompt()
    paraphrase = need_paraphrase(instruction)
    instruction = ins_paraphrase_helper(instruction) if paraphrase else instruction
    
    return instruction


def ss_evaluation_indicator(model, masked_instruction, debug):
    '''
    Usage: safety_indicator = ss_evaluation_indicator(model, masked_instruction, debug)
    '''
    GRMP_instance = base_prompt.GPTResponseMaskWordPrompt()
    model_input = GRMP_instance.get_prompt(masked_instruction)
    model_out = model(model_input, debug=debug)
    safety_indicator = GRMP_instance.parse(model_out) in safety_eval.Safe_SubString().refusal_string
    return safety_indicator


def merge_and_shuffle_with_order(random_selection, masked_words):
    random.shuffle(random_selection)
    
    for k in range(2*len(random_selection)):
        masked_positions = sorted(random.sample(range(len(random_selection) + len(masked_words)), len(masked_words)))
        if all([p < (len(random_selection + masked_words)//2 + k // 8) for p in masked_positions]):
            break
    
    SWQ_sequence, m_idx, s_idx = [], 0, 0
    for i in range(len(random_selection+masked_words)):
        if m_idx < len(masked_words) and i == masked_positions[m_idx]:
            SWQ_sequence.append(masked_words[m_idx]); m_idx += 1
        else:
            SWQ_sequence.append(random_selection[s_idx]); s_idx += 1
        
    return SWQ_sequence, masked_positions


def exact_match_search(keyword):
    wiki_wiki = wikipediaapi.Wikipedia('MaskPrompt (merlin@example.com)', 'en')
    page = wiki_wiki.page(keyword)
    return page if page.exists() else None


def concat_sections(sections, level=1, result = ""):
    for i, s in enumerate(sections):
        result += f"{s.title}\n{s.text}\n\n"
        result += f"{concat_sections(s.sections, level + 1)}"
    return result


def generate_msk_wd_ins(attack_model, prompt_input, MaskPrompt_instance, debug):
    retry, re_exception = 0, True
    while retry < 5:
        try: 
            response = attack_model(prompt_input, debug=debug)
            response = attack_model.resp_parse(response)[0]
            masked_words, masked_instruction = MaskPrompt_instance.parse(response)    # masked_words is a List
            re_exception = False
            break
        except Exception as e:
            logger.exception(f"Catch the excetion: {e}\nRetrying...")
            retry += 1
    if re_exception:
        raise Exception("Fail to match the regulare expression after try 5 times!")  
    
    return masked_words, masked_instruction


def create_wiki_entry(instruction, keyword):
    create_wiki_prompt = base_prompt.GPTCreateWikiPrompt()
    prompt_input = create_wiki_prompt.get_prompt(instruction, keyword)
    simulation_model = model_utils.load_model('gpt-4o', temperature=0.9, api_idx=0)
    retry, re_exception = 0, True
    while retry < 8:
        try:
            response = simulation_model(prompt_input, debug=False)
            response = simulation_model.resp_parse(response)[0]
            wiki_entry = create_wiki_prompt.parse(response)
            re_exception = False
            break
        except Exception as e:
            logger.exception(f"Catch the excetion: {e}\nRetrying...")
            retry += 1
    if re_exception:
        page = exact_match_search(keyword)
        if page:
            summary, sections = page.summary, page.sections
            first_second = concat_sections(sections[:2])
            wiki_entry = f"{summary}\n\n{first_second}"
        else:
            wiki_entry = response
        # raise Exception("Fail to match the regulare expression after try 5 times!")  
    
    return wiki_entry


def para_to_wiki(msk_instruction):
    para_to_wiki_prompt = base_prompt.GPTParaToWikiPrompt()
    prompt_input = para_to_wiki_prompt.get_prompt(msk_instruction)
    attack_model = model_utils.load_model('gpt-3.5-turbo', temperature=0.9, api_idx=0)
    response = attack_model(prompt_input, debug=False)
    response = attack_model.resp_parse(response)[0]
    masked_instruction = para_to_wiki_prompt.parse(response)
    return masked_instruction


def single_inference(args, idx, api_idx, ps, defense, attack_mname, target_mname, instruction, debug=False):
    
    defender = Defender(defense)                                                  # defense: None, ppl, para, retok

    args.wiki_dict_path = './src/wiki_entry.json'
    with open(args.wiki_dict_path, 'r') as fr:
        wiki_dict = json.load(fr)
        wiki_dict_keys = wiki_dict.keys()
        
    if ps == 'swq-mask' or ps == 'swq-mask-sw':                                   # 4 bases v.s. 1 ensemble; swq-mask is our convention name, which can be alias of swq-mask-sw.
        
        random_selection = random_choose(args.num_selections)
        instruction = ins_paraphrase(instruction)
        
        MwPrompt_instance = base_prompt.GPTMaskWordPrompt()
        prompt_input = MwPrompt_instance.get_prompt(instruction)

        attack_model = model_utils.load_model(attack_mname, temperature=args.temperature, api_idx=api_idx)
        
        # response = attack_model(prompt_input, debug=debug)
        # response = attack_model.resp_parse(response)[0]
        # masked_word, masked_instruction = MwPrompt_instance.parse(response)      # masked_word is a List
        masked_word, masked_instruction = generate_msk_wd_ins(attack_model, prompt_input, MwPrompt_instance, debug)

        SWQ_sequence = list(set(random_selection + masked_word))                 # SWQ means sequence word query
        for i in range(len(random_selection)):
            random.shuffle(SWQ_sequence)
            pos = [SWQ_sequence.index(word) + 1 for word in masked_word][0]
            if pos < (len(SWQ_sequence)//2 + i // 3):
                break
        
        attack_prompt = base_prompt.SWQAttackPrompt_sw().get_prompt(masked_instruction, SWQ_sequence, pos)
        victim_model = model_utils.load_model(target_mname, temperature=args.temperature, api_idx=api_idx)
        response = defender.handler(victim_model, attack_prompt)
        resp_list = [response]
        
        # print(Fore.GREEN + f">>> The attack prompt in {ps} prompt setting is:\n{attack_prompt}" + Fore.RESET)
        # print(Fore.MAGENTA + f">>> The response is:\n{response}" + Fore.RESET)

        res = {
            'idx': idx,
            'instruction': instruction,
            'msk_words': masked_word,
            'msk_instruction': masked_instruction,
            'resp_list': resp_list,
            'mask_choice': 'mask-sw', 
            # auxilary
            'SWQ_sequence': SWQ_sequence,
            'pos': pos,
            'response': response   
        }
        # sw: single word; mw: multiple words; sp: single phrase; mp: multiple phrase
        
    elif ps == 'swq-mask-sp':
        
        random_selection = random_choose(args.num_selections)
        instruction = ins_paraphrase(instruction)
        
        MpPrompt_instance = base_prompt.GPTMaskPhrasePrompt()
        prompt_input = MpPrompt_instance.get_prompt(instruction)

        attack_model = model_utils.load_model(attack_mname, temperature=args.temperature, api_idx=api_idx)
        
        retry, re_exception = 0, True
        while retry < 5:
            try: 
                response = attack_model(prompt_input, debug=debug)
                response = attack_model.resp_parse(response)[0]
                masked_word, masked_instruction = MpPrompt_instance.parse(response)      # masked_word is a List. Actually, we mask a phrase (see the GPTMaskPhrasePrompt), although we did not use masked_phrase as varible name.)
                re_exception = False
                break
            except Exception as e:
                logger.exception(f"Catch the excetion: {e}\nRetrying...")
                retry += 1
        if re_exception:
            raise Exception("Fail to match the regulare expression after try 5 times!")          

        SWQ_sequence = list(set(random_selection + masked_word))                 # SWQ means sequence word query
        for i in range(len(random_selection)):
            random.shuffle(SWQ_sequence)
            pos = [SWQ_sequence.index(word) + 1 for word in masked_word][0]
            if pos < (len(SWQ_sequence)//2 + i // 3):
                break
        
        attack_prompt = base_prompt.SWQAttackPrompt_sp().get_prompt(masked_instruction, SWQ_sequence, pos)
        victim_model = model_utils.load_model(target_mname, temperature=args.temperature, api_idx=api_idx)
        response = defender.handler(victim_model, attack_prompt)
        resp_list = [response]
        
        # print(Fore.GREEN + f">>> The attack prompt in {ps} prompt setting is:\n{attack_prompt}" + Fore.RESET)
        # print(Fore.MAGENTA + f">>> The response is:\n{response}" + Fore.RESET)

        res = {
            'idx': idx,
            'instruction': instruction,
            'msk_words': masked_word,
            'msk_instruction': masked_instruction,
            'resp_list': resp_list,
            'mask_choice': 'mask-sp', 
            # auxilary
            'SWQ_sequence': SWQ_sequence,
            'pos': pos,
            'response': response   
        }
        
    elif ps == 'swq-mask-mw':
        random_selection = random_choose(args.num_selections)
        instruction = ins_paraphrase(instruction)
        
        MwsPrompt_instance = base_prompt.GPTMaskWordsPrompt()
        prompt_input = MwsPrompt_instance.get_prompt(instruction)

        attack_model = model_utils.load_model(attack_mname, temperature=args.temperature, api_idx=api_idx)
        
        retry, re_exception = 0, True
        while retry < 5:
            try: 
                response = attack_model(prompt_input, debug=debug)
                response = attack_model.resp_parse(response)[0]
                masked_words, masked_instruction = MwsPrompt_instance.parse(response)    # masked_words is a List
                re_exception = False
                break
            except Exception as e:
                logger.exception(f"Catch the excetion: {e}\nRetrying...")
                retry += 1
        if re_exception:
            raise Exception("Fail to match the regulare expression after try 5 times!")          
        
        SWQ_sequence, masked_positions = merge_and_shuffle_with_order(random_selection, masked_words)
        pos = [SWQ_sequence.index(word) + 1 for word in masked_words]
        assert pos == [masked_position + 1 for masked_position in masked_positions]

        attack_prompt = base_prompt.SWQAttackPrompt_mw().get_prompt(masked_instruction, SWQ_sequence, pos)    
        victim_model = model_utils.load_model(target_mname, temperature=args.temperature, api_idx=api_idx)
        response = defender.handler(victim_model, attack_prompt)
        resp_list = [response]
        
        # print(Fore.GREEN + f"attack prompt in {ps} prompt setting is: {attack_prompt}" + Fore.RESET)
        # print(Fore.MAGENTA +  response + Fore.RESET)

        res = {
            'idx': idx,
            'instruction': instruction,
            'msk_words': masked_words,
            'msk_instruction': masked_instruction,
            'resp_list': resp_list,
            'mask_choice': 'mask-sw', 
            # auxilary
            'SWQ_sequence': SWQ_sequence,
            'pos': pos,
            'response': response   
        }
        
    elif ps == 'swq-mask-mp':
        random_selection = random_choose(args.num_selections)
        instruction = ins_paraphrase(instruction)
        
        MpsPrompt_instance = base_prompt.GPTMaskPhrasesPrompt() 
        prompt_input = MpsPrompt_instance.get_prompt(instruction)

        attack_model = model_utils.load_model(attack_mname, temperature=args.temperature, api_idx=api_idx)
        
        # response = attack_model(prompt_input, debug=debug)
        # response = attack_model.resp_parse(response)[0]
        # masked_words, masked_instruction = MpsPrompt_instance.parse(response)    # masked_words is a List
        masked_words, masked_instruction = generate_msk_wd_ins(attack_model, prompt_input, MpsPrompt_instance, debug)
        
        SWQ_sequence, masked_positions = merge_and_shuffle_with_order(random_selection, masked_words)
        pos = [SWQ_sequence.index(word) + 1 for word in masked_words]
        assert pos == [masked_position + 1 for masked_position in masked_positions]

        attack_prompt = base_prompt.SWQAttackPrompt_mp().get_prompt(masked_instruction, SWQ_sequence, pos)    
        victim_model = model_utils.load_model(target_mname, temperature=args.temperature, api_idx=api_idx)
        response = defender.handler(victim_model, attack_prompt)
        resp_list = [response]
        
        # print(Fore.GREEN + f"attack prompt in {ps} prompt setting is: {attack_prompt}" + Fore.RESET)
        # print(Fore.MAGENTA +  response + Fore.RESET)

        res = {
            'idx': idx,
            'instruction': instruction,
            'msk_words': masked_words,
            'msk_instruction': masked_instruction,
            'resp_list': resp_list,
            'mask_choice': 'mask-sw', 
            # auxilary
            'SWQ_sequence': SWQ_sequence,
            'pos': pos,
            'response': response   
        }  

###########################################################################
    elif ps == 'wiki-text-infilling-sw':
        # Select single masked word
        MwPrompt_instance = base_prompt.GPTMaskWordPrompt()
        prompt_input = MwPrompt_instance.get_prompt(instruction)

        attack_model = model_utils.load_model(attack_mname, temperature=args.temperature, api_idx=api_idx)
        
        # response = attack_model(prompt_input, debug=debug)
        # response = attack_model.resp_parse(response)[0]
        # masked_word, masked_instruction = MwPrompt_instance.parse(response)      # masked_word is a List 
        masked_word, masked_instruction = generate_msk_wd_ins(attack_model, prompt_input, MwPrompt_instance, debug)      # masked_word is a List 
        print(f'-------------{masked_instruction}')

        if masked_word[0] in wiki_dict_keys:
            wiki_entry = wiki_dict[masked_word[0]]
            print(Fore.LIGHTRED_EX + '# Re-use wiki entry....' + Fore.RESET)
        else:
            wiki_entry = create_wiki_entry(masked_instruction, masked_word[0])
            candidate = {f'{masked_word[0]}':f'{wiki_entry.strip()}'}
            wiki_dict.update(candidate)
            print(Fore.LIGHTRED_EX + '$ Create a new wiki entry....' + Fore.RESET)
        # # Construct the concept of masked words/phrase via LLM
        # wiki_entry = create_wiki_entry(masked_instruction, masked_word[0])
        paragraphs_ = re.split(r'\n{2,}', wiki_entry.strip())
        paragraphs = [p.strip() for p in paragraphs_ if p.strip()]
        first_s_t = "\n".join(paragraphs[:3])
        fourth_f_s = "\n".join(paragraphs[4:])
        summary, first_second, third_fourth = '', first_s_t, fourth_f_s
        
        # Construct attack prompt, peform attack and get the response
        attack_prompt = base_prompt.GPTTextInfillPrompt().get_prompt(para_to_wiki(masked_instruction), summary, first_second, third_fourth)
        victim_model = model_utils.load_model(target_mname, temperature=args.temperature, api_idx=api_idx)
        response = defender.handler(victim_model, attack_prompt)
        resp_list = [response]

        # print(Fore.GREEN + f">>> The attack prompt in {ps} prompt setting is:\n{attack_prompt}" + Fore.RESET)
        # print(Fore.MAGENTA + f">>> The response is:\n{response}" + Fore.RESET)

        res = {
            'idx': idx,
            'instruction': instruction,
            'msk_words': masked_word,
            'msk_instruction': masked_instruction,
            'resp_list': resp_list,
            'mask_choice': 'mask-sw', 
        }
        
    elif ps == 'wiki-text-infilling-sp':
        # Select single masked phrase
        MpPrompt_instance = base_prompt.GPTMaskPhrasePrompt()
        prompt_input = MpPrompt_instance.get_prompt(instruction)
        
        attack_model = model_utils.load_model(attack_mname, temperature=args.temperature, api_idx=api_idx)
        
        # response = attack_model(prompt_input, debug=debug)
        # response = attack_model.resp_parse(response)[0]
        # masked_word, masked_instruction = MpPrompt_instance.parse(response)      # masked_word is a List. Again, actually, we mask a phrase.
        masked_word, masked_instruction = generate_msk_wd_ins(attack_model, prompt_input, MpPrompt_instance, debug)      # masked_word is a List. Again, actually, we mask a phrase.
        print(f'-------------{masked_instruction}')

        if masked_word[0] in wiki_dict_keys:
            wiki_entry = wiki_dict[masked_word[0]]
            print(Fore.LIGHTRED_EX + '# Re-use wiki entry....' + Fore.RESET)
        else:
            wiki_entry = create_wiki_entry(masked_instruction, masked_word[0])
            candidate = {f'{masked_word[0]}':f'{wiki_entry.strip()}'}
            wiki_dict.update(candidate)
            print(Fore.LIGHTRED_EX + '$ Create a new wiki entry....' + Fore.RESET)
        # # Construct the concept of masked words/phrase via LLM
        # wiki_entry = create_wiki_entry(masked_instruction, masked_word[0])
        paragraphs_ = re.split(r'\n{2,}', wiki_entry.strip())
        paragraphs = [p.strip() for p in paragraphs_ if p.strip()]
        first_s_t = "\n".join(paragraphs[:3])
        fourth_f_s = "\n".join(paragraphs[4:])
        summary, first_second, third_fourth = '', first_s_t, fourth_f_s
        
        # Construct attack prompt, peform attack and get the response
        attack_prompt = base_prompt.GPTTextInfillPrompt().get_prompt(para_to_wiki(masked_instruction), summary, first_second, third_fourth)
        victim_model = model_utils.load_model(target_mname, temperature=args.temperature, api_idx=api_idx)
        response = defender.handler(victim_model, attack_prompt)
        resp_list = [response]

        # print(Fore.GREEN + f">>> The attack prompt in {ps} prompt setting is:\n{attack_prompt}" + Fore.RESET)
        # print(Fore.MAGENTA + f">>> The response is:\n{response}" + Fore.RESET)

        res = {
            'idx': idx,
            'instruction': instruction,
            'msk_words': masked_word,
            'msk_instruction': masked_instruction,
            'resp_list': resp_list,
            'mask_choice': 'mask-sp', 
        }

    elif ps == 'wiki-text-infilling-mw':
        # Select multiple masked words
        MwsPrompt_instance = base_prompt.GPTMaskWordsPrompt()
        prompt_input = MwsPrompt_instance.get_prompt(instruction)
        
        attack_model = model_utils.load_model(attack_mname, temperature=args.temperature, api_idx=api_idx)
        victim_model = model_utils.load_model(target_mname, temperature=args.temperature, api_idx=api_idx)
        
        # response = attack_model(prompt_input, debug=debug)
        # response = attack_model.resp_parse(response)[0]
        # masked_words_, masked_instruction_ = MwsPrompt_instance.parse(response)    # masked_words is a List  
        masked_words_, masked_instruction_ = generate_msk_wd_ins(attack_model, prompt_input, MwsPrompt_instance, debug)  # masked_words is a List
        
        resp_list, masked_instruction_list = [], []

        for masked_word in masked_words_:
            if masked_word in wiki_dict_keys:
                wiki_entry = wiki_dict[masked_word]
                print(Fore.LIGHTRED_EX + '# Re-use wiki entry....' + Fore.RESET)
            else:
                wiki_entry = create_wiki_entry(instruction.replace(masked_word, '[MASK]'), masked_word)
                candidate = {f'{masked_word}':f'{wiki_entry.strip()}'}
                wiki_dict.update(candidate)
                print(Fore.LIGHTRED_EX + '$ Create a new wiki entry....' + Fore.RESET)
            # # Construct context: construct the concept of masked words/phrase via LLM
            # wiki_entry = create_wiki_entry(instruction.replace(masked_word, '[MASK]'), masked_word)
            paragraphs_ = re.split(r'\n{2,}', wiki_entry.strip())
            paragraphs = [p.strip() for p in paragraphs_ if p.strip()]
            first_s_t = "\n".join(paragraphs[:3])
            fourth_f_s = "\n".join(paragraphs[4:])
            summary, first_second, third_fourth = '', first_s_t, fourth_f_s

            # Construct attack prompt, peform attack and get the response
            masked_instruction = instruction.replace(masked_word, '[MASK]')
            print(f'-------------{masked_instruction}')
            attack_prompt = base_prompt.GPTTextInfillPrompt().get_prompt(para_to_wiki(masked_instruction), summary, first_second, third_fourth)
            response = defender.handler(victim_model, attack_prompt)
            resp_list.append(response)

            # print(Fore.GREEN + f">>> The attack prompt in {ps} prompt setting is:\n{attack_prompt}" + Fore.RESET)
            # print(Fore.MAGENTA + f">>> The response is:\n{response}" + Fore.RESET)
            
            masked_instruction_list.append(masked_instruction)
                 
        res = {
            'idx': idx,
            'instruction': instruction,
            'msk_words': masked_words_,
            'msk_instruction': masked_instruction_list,
            'resp_list': resp_list,
            'mask_choice': 'mask-mw', 
        }  
        
    elif ps == 'wiki-text-infilling-mp':
        # Select multiple masked phrases
        MpsPrompt_instance = base_prompt.GPTMaskPhrasesPrompt() 
        prompt_input = MpsPrompt_instance.get_prompt(instruction)  
        
        attack_model = model_utils.load_model(attack_mname, temperature=args.temperature, api_idx=api_idx)
        victim_model = model_utils.load_model(target_mname, temperature=args.temperature, api_idx=api_idx)
        
        # response = attack_model(prompt_input, debug=debug)
        # response = attack_model.resp_parse(response)[0]
        # masked_words_, masked_instruction_ = MpsPrompt_instance.parse(response)    # masked_words is a List    
        masked_words_, masked_instruction_ = generate_msk_wd_ins(attack_model, prompt_input, MpsPrompt_instance, debug)  # masked_words is a List 
        
        resp_list, masked_instruction_list = [], []

        for masked_word in masked_words_:
            if masked_word in wiki_dict_keys:
                wiki_entry = wiki_dict[masked_word]
                print(Fore.LIGHTRED_EX + '# Re-use wiki entry....' + Fore.RESET)
            else:
                wiki_entry = create_wiki_entry(instruction.replace(masked_word, '[MASK]'), masked_word)
                candidate = {f'{masked_word}':f'{wiki_entry.strip()}'}
                wiki_dict.update(candidate)
                print(Fore.LIGHTRED_EX + '$ Create a new wiki entry....' + Fore.RESET)
            # # Construct context: construct the concept of masked words/phrase via LLM
            # wiki_entry = create_wiki_entry(instruction.replace(masked_word, '[MASK]'), masked_word)
            paragraphs_ = re.split(r'\n{2,}', wiki_entry.strip())
            paragraphs = [p.strip() for p in paragraphs_ if p.strip()]
            first_s_t = "\n".join(paragraphs[:3])
            fourth_f_s = "\n".join(paragraphs[4:])
            summary, first_second, third_fourth = '', first_s_t, fourth_f_s

            # Construct attack prompt, peform attack and get the response
            masked_instruction = instruction.replace(masked_word, '[MASK]')
            print(f'-------------{masked_instruction}')
            attack_prompt = base_prompt.GPTTextInfillPrompt().get_prompt(para_to_wiki(masked_instruction), summary, first_second, third_fourth)
            response = defender.handler(victim_model, attack_prompt)
            resp_list.append(response)

            # print(Fore.GREEN + f">>> The attack prompt in {ps} prompt setting is:\n{attack_prompt}" + Fore.RESET)
            # print(Fore.MAGENTA + f">>> The response is:\n{response}" + Fore.RESET)
            
            masked_instruction_list.append(masked_instruction)
        
        res = {
            'idx': idx,
            'instruction': instruction,
            'msk_words': masked_words_,
            'msk_instruction': masked_instruction_list,
            'resp_list': resp_list,
            'mask_choice': 'mask-mp', 
        }         
      
###########################################################################

    elif ps in ['naive-swq-mask-sw', 'naive-swq-mask-sp']:

        print(Fore.RED + 'HERE!' + Fore.RESET)
        random_selection = random_choose(args.num_selections)
        instruction = ins_paraphrase(instruction)
        
        MwPrompt_instance = base_prompt.GPTMaskWordPrompt() if ps == 'naive-swq-mask-sw' else base_prompt.GPTMaskPhrasePrompt()
        print(Fore.RED + f"{ps=='naive-swq-mask-sw'}" + Fore.RESET)
        prompt_input = MwPrompt_instance.get_prompt(instruction)
        attack_model = model_utils.load_model(attack_mname, temperature=args.temperature, api_idx=api_idx)
        masked_word, masked_instruction = generate_msk_wd_ins(attack_model, prompt_input, MwPrompt_instance, debug)

        SWQ_sequence = list(set(random_selection + masked_word))                 # SWQ means sequence word query
        for i in range(len(random_selection)):
            random.shuffle(SWQ_sequence)
            pos = [SWQ_sequence.index(word) + 1 for word in masked_word][0]
            if pos < (len(SWQ_sequence)//2 + i // 3):
                break

        attack_prompt = base_prompt.AttackPrompt_naive().get_prompt(masked_instruction, SWQ_sequence, pos)
        victim_model = model_utils.load_model(target_mname, temperature=args.temperature, api_idx=api_idx)
        response = defender.handler(victim_model, attack_prompt)
        resp_list = [response]
        
        print(Fore.GREEN + f">>> The attack prompt in {ps} prompt setting is:\n{attack_prompt}" + Fore.RESET)
        print(Fore.MAGENTA + f">>> The response is:\n{response}" + Fore.RESET)

        res = {
            'idx': idx,
            'instruction': instruction,
            'msk_words': masked_word,
            'msk_instruction': masked_instruction,
            'resp_list': resp_list,
            'mask_choice': 'naive-mask', 
            # auxilary
            'SWQ_sequence': SWQ_sequence,
            'pos': pos,
            'response': response   
        }
        # sw: single word; mw: multiple words; sp: single phrase; mp: multiple phrase

    else: 
        raise NotImplementedError
    
    with open(args.wiki_dict_path, 'w') as fw:
        json.dump(wiki_dict, fw, indent=4)
        
    defender.end_handler()
    return res, attack_prompt
