
# python src/main.py \
#     --input_dataset jbb \
#     --victim_model_name gpt-4o-mini \
#     --judge_model_name gpt-4o \
#     --ps swq-mask-sw \
#     --model_name gpt-4o \
#     --mode 7 \
#     --temperature 0.6 \
#     --num_samples 2


python src/main.py \
    --input_dataset 'jbb' \
    --victim_model_name 'gpt-4o-mini' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-sw' \
    --model_name 'gpt-4o' \
    --mode 4 \
    --temperature 0.6 \
    --num_samples 2


###########################################################################

# python src/main.py \
#     --input_dataset jbb \
#     --victim_model_name llama3-api-70b \
#     --judge_model_name gpt-4o \
#     --ps swq-mask-sw \
#     --model_name gpt-4o \
#     --mode 4 \

# python src/main.py \
#     --input_dataset jbb \
#     --victim_model_name llama3-api-70b \
#     --judge_model_name gpt-4o \
#     --ps swq-mask-sp \
#     --model_name gpt-4o \
#     --mode 4 \

# python src/main.py \
#     --input_dataset jbb \
#     --victim_model_name llama3-api-70b \
#     --judge_model_name gpt-4o \
#     --ps swq-mask-mw \
#     --model_name gpt-4o \
#     --mode 4 \

# python src/main.py \
#     --input_dataset jbb \
#     --victim_model_name llama3-api-70b \
#     --judge_model_name gpt-4o \
#     --ps swq-mask-mp \
#     --model_name gpt-4o \
#     --mode 4 \



