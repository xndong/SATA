# sw
python src/main.py \
    --input_dataset jbb \
    --victim_model_name gpt-4o \
    --judge_model_name gpt-4o \
    --ps swq-mask-sw \
    --model_name gpt-4o \
    --mode 3 \
    --exp_id 12_07-21_06_14 


# sp
python src/main.py \
    --input_dataset jbb \
    --victim_model_name gpt-4o \
    --judge_model_name gpt-4o \
    --ps swq-mask-sp \
    --model_name gpt-4o \
    --mode 3 \
    --exp_id 12_07-21_15_10 


# mw
python src/main.py \
    --input_dataset jbb \
    --victim_model_name gpt-4o \
    --judge_model_name gpt-4o \
    --ps swq-mask-mw \
    --model_name gpt-4o \
    --mode 3 \
    --exp_id 12_07-21_25_19 


# mp
python src/main.py \
    --input_dataset jbb \
    --victim_model_name gpt-4o \
    --judge_model_name gpt-4o \
    --ps swq-mask-mp \
    --model_name gpt-4o \
    --mode 3 \
    --exp_id 12_07-21_37_55
