# sw
python src/main.py \
    --input_dataset advbench-custom \
    --victim_model_name gpt-4o-mini \
    --judge_model_name gpt-4o \
    --ps swq-mask-sw \
    --model_name gpt-4o \
    --mode 7 \
    --temperature 0.6 


# sp
python src/main.py \
    --input_dataset advbench-custom \
    --victim_model_name gpt-4o-mini \
    --judge_model_name gpt-4o \
    --ps swq-mask-sp \
    --model_name gpt-4o \
    --mode 7 \
    --temperature 0.6 


# mw
python src/main.py \
    --input_dataset advbench-custom \
    --victim_model_name gpt-4o-mini \
    --judge_model_name gpt-4o \
    --ps swq-mask-mw \
    --model_name gpt-4o \
    --mode 7 \
    --temperature 0.6 


# mp
python src/main.py \
    --input_dataset advbench-custom \
    --victim_model_name gpt-4o-mini \
    --judge_model_name gpt-4o \
    --ps swq-mask-mp \
    --model_name gpt-4o \
    --mode 7 \
    --temperature 0.6 

