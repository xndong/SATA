# sw
python src/main.py \
    --input_dataset 'advbench-custom' \
    --victim_model_name 'llama3-api-8b' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-sw' \
    --model_name 'gpt-4o' \
    --mode 7


# sp
python src/main.py \
    --input_dataset 'advbench-custom' \
    --victim_model_name 'llama3-api-8b' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-sp' \
    --model_name 'gpt-4o' \
    --mode 7


# mw
python src/main.py \
    --input_dataset 'advbench-custom' \
    --victim_model_name 'llama3-api-8b' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-mw' \
    --model_name 'gpt-4o' \
    --mode 7


# mp
python src/main.py \
    --input_dataset 'advbench-custom' \
    --victim_model_name 'llama3-api-8b' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-mp' \
    --model_name 'gpt-4o' \
    --mode 7

