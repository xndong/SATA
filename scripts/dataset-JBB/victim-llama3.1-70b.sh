# sw
python src/main.py \
    --input_dataset jbb \
    --victim_model_name llama3-api-70b \
    --judge_model_name gpt-4o \
    --ps swq-mask-sw \
    --model_name gpt-4o \
    --mode 3 \
    --temperature 0.6 \
    --exp_id 12_05-15_03_20


# sp
python src/main.py \
    --input_dataset jbb \
    --victim_model_name llama3-api-70b \
    --judge_model_name gpt-4o \
    --ps swq-mask-sp \
    --model_name gpt-4o \
    --mode 3 \
    --temperature 0.6 \
    --exp_id 12_05-15_15_47


# mw
python src/main.py \
    --input_dataset jbb \
    --victim_model_name llama3-api-70b \
    --judge_model_name gpt-4o \
    --ps swq-mask-mw \
    --model_name gpt-4o \
    --mode 3 \
    --temperature 0.6 \
    --exp_id 12_05-15_41_21


# mp
python src/main.py \
    --input_dataset jbb \
    --victim_model_name llama3-api-70b \
    --judge_model_name gpt-4o \
    --ps swq-mask-mp \
    --model_name gpt-4o \
    --mode 3 \
    --temperature 0.6 \
    --exp_id 12_05-15_58_32
