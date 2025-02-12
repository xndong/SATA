# sw
python src/main.py \
    --input_dataset advbench-custom \
    --victim_model_name gpt-3.5-turbo \
    --judge_model_name gpt-4o \
    --ps swq-mask-sw \
    --model_name gpt-4o \
    --mode 7 


# sp
python src/main.py \
    --input_dataset advbench-custom \
    --victim_model_name gpt-3.5-turbo \
    --judge_model_name gpt-4o \
    --ps swq-mask-sp \
    --model_name gpt-4o \
    --mode 7 


# mw
python src/main.py \
    --input_dataset advbench-custom \
    --victim_model_name gpt-3.5-turbo \
    --judge_model_name gpt-4o \
    --ps swq-mask-mw \
    --model_name gpt-4o \
    --mode 7 


# mp
python src/main.py \
    --input_dataset advbench-custom \
    --victim_model_name gpt-3.5-turbo \
    --judge_model_name gpt-4o \
    --ps swq-mask-mp \
    --model_name gpt-4o \
    --mode 7 


