import os, sys
import json, jsonlines
import csv
import time, copy
from datetime import datetime
from colorama import Fore
from tqdm.auto import tqdm
import multiprocessing as mp

sys.path.append('./')
sys.path.append('../')
from utility.argsparse import parse_args
import utility.logger
import src.safe_eval as safety_eval
from attack_wiki import single_inference


def load_dataset(args):
    
    benchmark_dict = {
        "advbench-custom" : "advbench/harmful_behaviors_custom.csv",
        "advbench" : "advbench/harmful_behaviors.csv",
        "jbb":"JailbreakBench/JBB-harmful-behaviors.csv"
    }
    BENCHMARK_DIR = os.path.join(args.input_dir, benchmark_dict[args.input_dataset])
    with open(BENCHMARK_DIR, 'r') as f:
        if args.input_dataset == 'advbench-custom':
            reader = csv.reader(f)
            data = list(reader)[1:]         # the first line is the header
            assert len(data) == 50
            data = [d[1] for d in data]
            print(Fore.LIGHTGREEN_EX + f"Using harmful_behaviors_custom dataset." + Fore.RESET)
        elif args.input_dataset == 'advbench':
            reader = csv.reader(f)
            data = list(reader)[1:]         # the first line is the header
            assert len(data) == 520
            data = [d[0] for d in data]
            print(Fore.LIGHTGREEN_EX + f"Using harmful_behaviors dataset." + Fore.RESET) 
        elif args.input_dataset == 'jbb':
            reader = csv.reader(f)
            data = list(reader)[1:]         # the first line is the header
            assert len(data) == 100
            data = [d[1] for d in data]
            print(Fore.LIGHTGREEN_EX + f"Using JBB-harmful-behaviors dataset." + Fore.RESET)            
        else:
            raise NotImplementedError("other dataset not implemented yet")
    
    return data

def load_data_category(args):

    benchmark_dict = {
        "jbb":"JailbreakBench/JBB-harmful-behaviors.csv"
    }
    BENCHMARK_DIR = os.path.join(args.input_dir, benchmark_dict[args.input_dataset])
    with open(BENCHMARK_DIR, 'r') as f:
        if args.input_dataset == 'jbb':
            reader = csv.reader(f)
            data = list(reader)[1:]         # the first line is the header
            assert len(data) == 100
            data_ca = [d[4] for d in data]    # category column
            data_be = [d[3] for d in data]    # behavior column
            print(Fore.LIGHTGREEN_EX + f"Load JBB-harmful-behaviors dataset categories and behaviors." + Fore.RESET) 
        else: return [], []
    
    return data_ca, data_be


def main(args, logger):
    
    data = load_dataset(args)[:args.num_samples] if args.num_samples != -1 else load_dataset(args)
    logger.info(f"The length of dataset is {len(data)}.")
    if 'jbb' in args.input_dataset: data_ca, _ = load_data_category(args) 

    # Global setting of result file for inference and evaluation
    # result dir
    args.output_dir = args.output_dir.replace('save_dir_placeholder', f'{args.input_dataset}')
    if args.defense is not None:
        args.output_dir = args.output_dir + f'_[def-{args.defense}]'
    if not os.path.exists(args.output_dir): 
        os.makedirs(args.output_dir, exist_ok=True)
    # result name
    result_file_name = f'{args.input_dataset}-ps-{args.ps}_[att-{args.model_name}]_tar-{args.victim_model_name}'  # ps: prompt setting; att: attack model; tar: target model
    result_file_name += f'_def-{args.defense}' if args.defense is not None else ''                                # extra setting for defense
    result_file_name += f'_[num-{args.num_samples}]' if args.num_samples != -1 else ''                            # extra setting for num_samples
    result_file_name += f'_expID-{args.exp_id}'                                                                   # extra setting for exp_id to distinguish exps with sample settings.
    result_file_name += '.jsonl'
    # result path
    result_file_path = os.path.join(args.output_dir, result_file_name)
    
    '''
    # Uncomment if you would like to dump the attack prompt
    if args.defense == 'ppl':
        src_dir, ps_abbr, attack_prompt_dict = os.path.dirname(__file__), 'TextInfilling' if 'wiki-text-infilling' in args.ps else 'SWQ', {}
        args.att_prompt_path = f'{os.path.dirname(src_dir)}/dump-att-prompts/{ps_abbr}_{args.victim_model_name}_{args.ps[-2:]}.json'
        os.makedirs(os.path.dirname(args.att_prompt_path), exist_ok=True)
    '''
                    
    # Inference
    if args.mode & 4:
        logger.notice(">>>>> Running inference")
        start_time = time.time()
        try:
            if args.num_processes == 1:
                api_idx = 0
                res = []
                for i in tqdm(range(len(data))):
                    res_i, attack_prompt_i = single_inference(args, i, api_idx, args.ps, args.defense, args.model_name, args.victim_model_name, data[i], debug=args.debug)
                    if args.input_dataset == 'jbb': res_i.update({'category':data_ca[i]})
                    res.append(res_i)
                    '''
                    # Uncomment if you would like to dump the attack prompt
                    if args.defense == 'ppl': attack_prompt_dict.update({data[i]:attack_prompt_i})
                    '''
                
            else:
                raise NotImplementedError

        except KeyboardInterrupt:
            logger.info("Interrupted by user")
            return
        end_time = time.time()
        logger.info(f"Time elapsed for inference: {end_time - start_time:.2f}s")
        
        # write result
        with open(result_file_path[:-1], 'w', encoding='utf-8') as f:   #.json
            json.dump(res, f, ensure_ascii=False, indent=4)
        
        '''
        # Uncomment if you would like to dump the attack prompt
        if args.defense == 'ppl': 
            with open(args.att_prompt_path, 'w') as fx:
                json.dump(attack_prompt_dict, fx, indent=4)
        '''
        
    # Eval
    # eval_ss
    if args.mode & 2:
        logger.notice(">>>>> Substring evaluation")
        with open(result_file_path[:-1], 'r') as f:
            res = json.load(f)

        safety_eval.ss_eval_handler(res, args.ps)
                
    # eval_llm
    if args.mode & 1 or args.mode == 8:                         # see safe_eval.py for "args.mode==8"
        logger.notice(">>>>> GPT-Judge evaluation")
        with open(result_file_path[:-1], 'r') as f:
            res = json.load(f)

        proc_res = safety_eval.gpt_eval_handler(res, args)      # safe_eval.py module

        # update file with score stored
        with open(result_file_path[:-1], 'w') as f:
            json.dump(proc_res, f, indent=4)    




if __name__ == "__main__":

    args = parse_args()
    args_dict = vars(args)

    logger = utility.logger.initialize_exp(args)
    # main(args, logger)
    try:
        main(args, logger)
    except Exception as e:
        print(f"error exception: {e}"); time.sleep(1)
        os.remove(args.logfile)   


'''
# Running Command:
##* fully or partially inference
python src/main.py --input_dataset advbench-custom --victim_model_name gpt-3.5-turbo --judge_model_name gpt-4o --ps swq-mask-sp --mode 7
python src/main.py --input_dataset advbench-custom --num_samples 10 --victim_model_name gpt-3.5-turbo --judge_model_name gpt-4o --ps swq-mask-sp --mode 7

##* ps[swq-mask-sw, swq-mask-sp...] + defense
python src/main.py --input_dataset advbench-custom --victim_model_name gpt-3.5-turbo --judge_model_name gpt-4o --ps swq-mask-sp --mode 7
python src/main.py --input_dataset advbench-custom --victim_model_name gpt-3.5-turbo --judge_model_name gpt-4o --ps swq-mask-sp --defense ppl --mode 7

##*  NOTE: mode 8,3,2,1 need to provide your previous exp_ID
python src/main.py --input_dataset advbench-custom --num_samples 10 --victim_model_name gpt-3.5-turbo --judge_model_name gpt-4o --ps swq-mask-sp --mode 8 --exp_id PASTE_YOUR_expID
python src/main.py --input_dataset advbench-custom --num_samples 10 --victim_model_name gpt-3.5-turbo --judge_model_name gpt-4o --ps swq-mask-sp --mode 3 --exp_id PASTE_YOUR_expID
python src/main.py --input_dataset advbench-custom --num_samples 10 --victim_model_name gpt-3.5-turbo --judge_model_name gpt-4o --ps swq-mask-sp --mode 2 --exp_id PASTE_YOUR_expID
python src/main.py --input_dataset advbench-custom --num_samples 10 --victim_model_name gpt-3.5-turbo --judge_model_name gpt-4o --ps swq-mask-sp --mode 1 --exp_id PASTE_YOUR_expID
'''