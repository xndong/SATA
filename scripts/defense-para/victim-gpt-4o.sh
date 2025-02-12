# sw
python src/main.py \
    --input_dataset advbench-custom \
    --victim_model_name gpt-4o \
    --judge_model_name gpt-4o \
    --ps swq-mask-sw \
    --model_name gpt-4o \
    --mode 7 \
    --defense para


# sp
python src/main.py \
    --input_dataset advbench-custom \
    --victim_model_name gpt-4o \
    --judge_model_name gpt-4o \
    --ps swq-mask-sp \
    --model_name gpt-4o \
    --mode 7 \
    --defense para


# mw
python src/main.py \
    --input_dataset advbench-custom \
    --victim_model_name gpt-4o \
    --judge_model_name gpt-4o \
    --ps swq-mask-mw \
    --model_name gpt-4o \
    --mode 7 \
    --defense para


# mp
python src/main.py \
    --input_dataset advbench-custom \
    --victim_model_name gpt-4o \
    --judge_model_name gpt-4o \
    --ps swq-mask-mp \
    --model_name gpt-4o \
    --mode 7 \
    --defense para