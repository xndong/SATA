# sw
python src/main.py \
    --input_dataset 'advbench-custom' \
    --victim_model_name 'gpt-4o' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-sw' \
    --model_name 'gpt-4o' \
    --mode 7 \
    --defense ppl


# sp
python src/main.py \
    --input_dataset 'advbench-custom' \
    --victim_model_name 'gpt-4o' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-sp' \
    --model_name 'gpt-4o' \
    --mode 7 \
    --defense ppl


# mw
python src/main.py \
    --input_dataset 'advbench-custom' \
    --victim_model_name 'gpt-4o' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-mw' \
    --model_name 'gpt-4o' \
    --mode 7 \
    --defense ppl


# mp
python src/main.py \
    --input_dataset 'advbench-custom' \
    --victim_model_name 'gpt-4o' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-mp' \
    --model_name 'gpt-4o' \
    --mode 7 \
    --defense ppl