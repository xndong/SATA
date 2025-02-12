# sw
knockknock telegram --token 7745411874:AAHqvL0TRSnVHeYdlAK9zs_1ZiQuaB4BNsw --chat-id 7294961734 \
python src/main.py \
    --input_dataset advbench-custom \
    --victim_model_name gpt-4o-mini \
    --judge_model_name gpt-4o \
    --ps swq-mask-sw \
    --model_name gpt-4o \
    --mode 7 \
    --temperature 0.6 


# sp
knockknock telegram --token 7745411874:AAHqvL0TRSnVHeYdlAK9zs_1ZiQuaB4BNsw --chat-id 7294961734 \
python src/main.py \
    --input_dataset advbench-custom \
    --victim_model_name gpt-4o-mini \
    --judge_model_name gpt-4o \
    --ps swq-mask-sp \
    --model_name gpt-4o \
    --mode 7 \
    --temperature 0.6 


# mw
knockknock telegram --token 7745411874:AAHqvL0TRSnVHeYdlAK9zs_1ZiQuaB4BNsw --chat-id 7294961734 \
python src/main.py \
    --input_dataset advbench-custom \
    --victim_model_name gpt-4o-mini \
    --judge_model_name gpt-4o \
    --ps swq-mask-mw \
    --model_name gpt-4o \
    --mode 7 \
    --temperature 0.6 


# mp
knockknock telegram --token 7745411874:AAHqvL0TRSnVHeYdlAK9zs_1ZiQuaB4BNsw --chat-id 7294961734 \
python src/main.py \
    --input_dataset advbench-custom \
    --victim_model_name gpt-4o-mini \
    --judge_model_name gpt-4o \
    --ps swq-mask-mp \
    --model_name gpt-4o \
    --mode 7 \
    --temperature 0.6 


# ensemble
knockknock telegram --token 7745411874:AAHqvL0TRSnVHeYdlAK9zs_1ZiQuaB4BNsw --chat-id 7294961734 \
python src/main.py \
    --input_dataset advbench-custom \
    --victim_model_name gpt-4o-mini \
    --judge_model_name gpt-4o \
    --ps swq-mask-ensemble \
    --model_name gpt-4o \
    --mode 7 \
    --temperature 0.6 
