


declare -a pss=('swq-mask-sw' 'swq-mask-sp' 'swq-mask-mw' 'swq-mask-mp')

# llama3-api-70b # 也不设置--temperature 0.6了
for ps in ${pss[@]};do
    echo -e "\033[35m ******** Current parameter setting is ${ps} ******** \033[0m"
    knockknock telegram --token 7745411874:AAHqvL0TRSnVHeYdlAK9zs_1ZiQuaB4BNsw --chat-id 7294961734 \
        python src/main.py --input_dataset advbench-custom --victim_model_name llama3-api-70b --judge_model_name gpt-4o --ps ${ps} --model_name gpt-4o --mode 7 --defense self-reminder
done

# claude-v2
for ps in ${pss[@]};do
    echo -e "\033[35m ******** Current parameter setting is ${ps} ******** \033[0m"
    knockknock telegram --token 7745411874:AAHqvL0TRSnVHeYdlAK9zs_1ZiQuaB4BNsw --chat-id 7294961734 \
        python src/main.py --input_dataset advbench-custom --victim_model_name claude-v2 --judge_model_name gpt-4o --ps ${ps} --model_name gpt-4o --mode 7 --defense self-reminder
done

gpt-4o
for ps in ${pss[@]};do
    echo -e "\033[35m ******** Current parameter setting is ${ps} ******** \033[0m"
    knockknock telegram --token 7745411874:AAHqvL0TRSnVHeYdlAK9zs_1ZiQuaB4BNsw --chat-id 7294961734 \
        python src/main.py --input_dataset advbench-custom --victim_model_name gpt-4o --judge_model_name gpt-4o --ps ${ps} --model_name gpt-4o --mode 7 --defense self-reminder
done

