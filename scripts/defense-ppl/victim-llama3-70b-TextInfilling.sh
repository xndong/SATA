# sw
python src/main.py \
    --input_dataset 'advbench-custom' \
    --victim_model_name 'llama3-api-70b' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-sw' \
    --model_name 'gpt-4o' \
    --mode 7 \
    --temperature 0.6 \
    --defense ppl


# sp
python src/main.py \
    --input_dataset 'advbench-custom' \
    --victim_model_name 'llama3-api-70b' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-sp' \
    --model_name 'gpt-4o' \
    --mode 7 \
    --temperature 0.6 \
    --defense ppl


# mw
python src/main.py \
    --input_dataset 'advbench-custom' \
    --victim_model_name 'llama3-api-70b' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-mw' \
    --model_name 'gpt-4o' \
    --mode 7 \
    --temperature 0.6 \
    --defense ppl


# mp
python src/main.py \
    --input_dataset 'advbench-custom' \
    --victim_model_name 'llama3-api-70b' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-mp' \
    --model_name 'gpt-4o' \
    --mode 7 \
    --temperature 0.6 \
    --defense ppl