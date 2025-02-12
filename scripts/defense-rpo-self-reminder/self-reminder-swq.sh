


declare -a pss=('swq-mask-sw' 'swq-mask-sp' 'swq-mask-mw' 'swq-mask-mp')

# llama3-api-70b 
for ps in ${pss[@]};do
    echo -e "\033[35m ******** Current parameter setting is ${ps} ******** \033[0m"
    python src/main.py --input_dataset advbench-custom --victim_model_name llama3-api-70b --judge_model_name gpt-4o --ps ${ps} --model_name gpt-4o --mode 7 --defense self-reminder
done

# claude-v2
for ps in ${pss[@]};do
    echo -e "\033[35m ******** Current parameter setting is ${ps} ******** \033[0m"
    python src/main.py --input_dataset advbench-custom --victim_model_name claude-v2 --judge_model_name gpt-4o --ps ${ps} --model_name gpt-4o --mode 7 --defense self-reminder
done

gpt-4o
for ps in ${pss[@]};do
    echo -e "\033[35m ******** Current parameter setting is ${ps} ******** \033[0m"
    python src/main.py --input_dataset advbench-custom --victim_model_name gpt-4o --judge_model_name gpt-4o --ps ${ps} --model_name gpt-4o --mode 7 --defense self-reminder
done

