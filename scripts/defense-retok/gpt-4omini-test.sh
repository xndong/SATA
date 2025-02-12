

# python src/main.py \
#     --input_dataset advbench-custom \
#     --victim_model_name gpt-4o-mini \
#     --judge_model_name gpt-4o \
#     --ps swq-mask-sw \
#     --model_name gpt-4o \
#     --mode 4 \
#     --defense retok \
#     --num_samples 2







python /gfshome/MaskPrompt/src/main.py \
    --input_dataset 'advbench-custom' \
    --victim_model_name 'gpt-4o-mini' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-sw' \
    --model_name 'gpt-4o' \
    --mode 4 \
    --defense retok \
    --num_samples 3


