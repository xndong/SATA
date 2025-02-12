# sw
knockknock telegram --token 7745411874:AAHqvL0TRSnVHeYdlAK9zs_1ZiQuaB4BNsw --chat-id 7294961734 \
python /gfshome/MaskPrompt/src/main.py \
    --input_dataset 'advbench-custom' \
    --victim_model_name 'claude-v2' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-sw' \
    --model_name 'gpt-4o' \
    --mode 7


# sp
knockknock telegram --token 7745411874:AAHqvL0TRSnVHeYdlAK9zs_1ZiQuaB4BNsw --chat-id 7294961734 \
python /gfshome/MaskPrompt/src/main.py \
    --input_dataset 'advbench-custom' \
    --victim_model_name 'claude-v2' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-sp' \
    --model_name 'gpt-4o' \
    --mode 7


# mw
knockknock telegram --token 7745411874:AAHqvL0TRSnVHeYdlAK9zs_1ZiQuaB4BNsw --chat-id 7294961734 \
python /gfshome/MaskPrompt/src/main.py \
    --input_dataset 'advbench-custom' \
    --victim_model_name 'claude-v2' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-mw' \
    --model_name 'gpt-4o' \
    --mode 7


# mp
knockknock telegram --token 7745411874:AAHqvL0TRSnVHeYdlAK9zs_1ZiQuaB4BNsw --chat-id 7294961734 \
python /gfshome/MaskPrompt/src/main.py \
    --input_dataset 'advbench-custom' \
    --victim_model_name 'claude-v2' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-mp' \
    --model_name 'gpt-4o' \
    --mode 7


# # ensemble
# knockknock telegram --token 7745411874:AAHqvL0TRSnVHeYdlAK9zs_1ZiQuaB4BNsw --chat-id 7294961734 \
# python /gfshome/MaskPrompt/src/main.py \
#     --input_dataset 'advbench-custom' \
#     --victim_model_name 'claude-v2' \
#     --judge_model_name 'gpt-4o' \
#     --ps 'wiki-text-infilling-ensemble' \
#     --model_name 'gpt-4o' \
#     --mode 7