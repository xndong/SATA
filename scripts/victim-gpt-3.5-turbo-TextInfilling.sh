# sw
python /gfshome/MaskPrompt/src/main.py \
    --input_dataset 'advbench-custom' \
    --victim_model_name 'gpt-3.5-turbo' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-sw' \
    --model_name 'gpt-4o' \
    --mode 7


# sp
python /gfshome/MaskPrompt/src/main.py \
    --input_dataset 'advbench-custom' \
    --victim_model_name 'gpt-3.5-turbo' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-sp' \
    --model_name 'gpt-4o' \
    --mode 7


# mw
python /gfshome/MaskPrompt/src/main.py \
    --input_dataset 'advbench-custom' \
    --victim_model_name 'gpt-3.5-turbo' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-mw' \
    --model_name 'gpt-4o' \
    --mode 7


# mp
python /gfshome/MaskPrompt/src/main.py \
    --input_dataset 'advbench-custom' \
    --victim_model_name 'gpt-3.5-turbo' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-mp' \
    --model_name 'gpt-4o' \
    --mode 7