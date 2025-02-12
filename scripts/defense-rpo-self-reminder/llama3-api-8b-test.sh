# declare -a pss=('swq-mask-sw' 'swq-mask-sp' 'swq-mask-mw' 'swq-mask-mp')
# declare -a pss=('wiki-text-infilling-sw' 'wiki-text-infilling-sp' 'wiki-text-infilling-mw' 'wiki-text-infilling-mp')



# ### rpo
# # test-1
# declare -a pss=('swq-mask-sw')
# for ps in ${pss[@]};do
#     echo -e "\033[35m ******** Current parameter setting is ${ps} ******** \033[0m"
#     knockknock telegram --token 7745411874:AAHqvL0TRSnVHeYdlAK9zs_1ZiQuaB4BNsw --chat-id 7294961734 \
#         python src/main.py --input_dataset advbench-custom --victim_model_name llama3-api-8b --judge_model_name gpt-4o --ps ${ps} --model_name gpt-4o --mode 7 --defense rpo
# done

# # test-2
# declare -a pss=('wiki-text-infilling-sw')
# for ps in ${pss[@]};do
#     echo -e "\033[35m ******** Current parameter setting is ${ps} ******** \033[0m"
#     knockknock telegram --token 7745411874:AAHqvL0TRSnVHeYdlAK9zs_1ZiQuaB4BNsw --chat-id 7294961734 \
#         python src/main.py --input_dataset advbench-custom --victim_model_name llama3-api-8b --judge_model_name gpt-4o --ps ${ps} --model_name gpt-4o --mode 7 --defense rpo
# done



# ## self-reminder
# # test-3
# declare -a pss=('swq-mask-sw')
# for ps in ${pss[@]};do
#     echo -e "\033[35m ******** Current parameter setting is ${ps} ******** \033[0m"
#     knockknock telegram --token 7745411874:AAHqvL0TRSnVHeYdlAK9zs_1ZiQuaB4BNsw --chat-id 7294961734 \
#         python src/main.py --input_dataset advbench-custom --victim_model_name llama3-api-8b --judge_model_name gpt-4o --ps ${ps} --model_name gpt-4o --mode 7 --defense self-reminder
# done

# # test-4
# declare -a pss=('wiki-text-infilling-sw')
# for ps in ${pss[@]};do
#     echo -e "\033[35m ******** Current parameter setting is ${ps} ******** \033[0m"
#     knockknock telegram --token 7745411874:AAHqvL0TRSnVHeYdlAK9zs_1ZiQuaB4BNsw --chat-id 7294961734 \
#         python src/main.py --input_dataset advbench-custom --victim_model_name llama3-api-8b --judge_model_name gpt-4o --ps ${ps} --model_name gpt-4o --mode 7 --defense self-reminder
# done



# 补充运行失败的实验
# python src/main.py --input_dataset advbench-custom --victim_model_name llama3-api-70b --judge_model_name gpt-4o --ps wiki-text-infilling-sw --model_name gpt-4o --mode 7 --defense rpo --exp_id 02_09-15_49_56
# python src/main.py --input_dataset advbench-custom --victim_model_name claude-v2 --judge_model_name gpt-4o --ps swq-mask-mw --model_name gpt-4o --mode 7 --defense rpo --exp_id 02_09-15_49_13
