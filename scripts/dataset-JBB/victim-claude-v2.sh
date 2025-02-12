# sw
python src/main.py \
    --input_dataset jbb \
    --victim_model_name claude-v2 \
    --judge_model_name gpt-4o \
    --ps swq-mask-sw \
    --model_name gpt-4o \
    --mode 3 \
    --exp_id 12_05-22_00_40


# sp
python src/main.py \
    --input_dataset jbb \
    --victim_model_name claude-v2 \
    --judge_model_name gpt-4o \
    --ps swq-mask-sp \
    --model_name gpt-4o \
    --mode 3 \
    --exp_id 12_05-22_13_34


# mw
python src/main.py \
    --input_dataset jbb \
    --victim_model_name claude-v2 \
    --judge_model_name gpt-4o \
    --ps swq-mask-mw \
    --model_name gpt-4o \
    --mode 3 \
    --exp_id 12_05-22_53_07


# mp
python src/main.py \
    --input_dataset jbb \
    --victim_model_name claude-v2 \
    --judge_model_name gpt-4o \
    --ps swq-mask-mp \
    --model_name gpt-4o \
    --mode 3 \
    --exp_id 12_05-23_12_56