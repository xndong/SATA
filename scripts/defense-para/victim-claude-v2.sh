# sw
knockknock telegram --token 7745411874:AAHqvL0TRSnVHeYdlAK9zs_1ZiQuaB4BNsw --chat-id 7294961734 \
python src/main.py \
    --input_dataset advbench-custom \
    --victim_model_name claude-v2 \
    --judge_model_name gpt-4o \
    --ps swq-mask-sw \
    --model_name gpt-4o \
    --mode 7 \
    --defense para


# sp
knockknock telegram --token 7745411874:AAHqvL0TRSnVHeYdlAK9zs_1ZiQuaB4BNsw --chat-id 7294961734 \
python src/main.py \
    --input_dataset advbench-custom \
    --victim_model_name claude-v2 \
    --judge_model_name gpt-4o \
    --ps swq-mask-sp \
    --model_name gpt-4o \
    --mode 7 \
    --defense para


# mw
knockknock telegram --token 7745411874:AAHqvL0TRSnVHeYdlAK9zs_1ZiQuaB4BNsw --chat-id 7294961734 \
python src/main.py \
    --input_dataset advbench-custom \
    --victim_model_name claude-v2 \
    --judge_model_name gpt-4o \
    --ps swq-mask-mw \
    --model_name gpt-4o \
    --mode 7 \
    --defense para


# mp
knockknock telegram --token 7745411874:AAHqvL0TRSnVHeYdlAK9zs_1ZiQuaB4BNsw --chat-id 7294961734 \
python src/main.py \
    --input_dataset advbench-custom \
    --victim_model_name claude-v2 \
    --judge_model_name gpt-4o \
    --ps swq-mask-mp \
    --model_name gpt-4o \
    --mode 7 \
    --defense para