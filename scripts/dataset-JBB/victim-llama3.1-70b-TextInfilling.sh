# sw
python /gfshome/MaskPrompt/src/main.py \
    --input_dataset 'jbb' \
    --victim_model_name 'llama3-api-70b' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-sw' \
    --model_name 'gpt-4o' \
    --mode 1 \
    --temperature 0.6 \
    --exp_id 12_10-22_36_12


# sp
python /gfshome/MaskPrompt/src/main.py \
    --input_dataset 'jbb' \
    --victim_model_name 'llama3-api-70b' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-sp' \
    --model_name 'gpt-4o' \
    --mode 7 \
    --temperature 0.6 


# mw
python /gfshome/MaskPrompt/src/main.py \
    --input_dataset 'jbb' \
    --victim_model_name 'llama3-api-70b' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-mw' \
    --model_name 'gpt-4o' \
    --mode 7 \
    --temperature 0.6 


# mp
python /gfshome/MaskPrompt/src/main.py \
    --input_dataset 'jbb' \
    --victim_model_name 'llama3-api-70b' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-mp' \
    --model_name 'gpt-4o' \
    --mode 7 \
    --temperature 0.6 