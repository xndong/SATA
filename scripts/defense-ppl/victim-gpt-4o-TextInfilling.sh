# sw
knockknock telegram --token 7830241625:AAGyvxLxAUMYle4AgITGjHPObRG0FZxUPkM --chat-id 7294961734 \
python /gfshome/MaskPrompt/src/main.py \
    --input_dataset 'advbench-custom' \
    --victim_model_name 'gpt-4o' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-sw' \
    --model_name 'gpt-4o' \
    --mode 7 \
    --defense ppl


# sp
knockknock telegram --token 7830241625:AAGyvxLxAUMYle4AgITGjHPObRG0FZxUPkM --chat-id 7294961734 \
python /gfshome/MaskPrompt/src/main.py \
    --input_dataset 'advbench-custom' \
    --victim_model_name 'gpt-4o' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-sp' \
    --model_name 'gpt-4o' \
    --mode 7 \
    --defense ppl


# mw
knockknock telegram --token 7830241625:AAGyvxLxAUMYle4AgITGjHPObRG0FZxUPkM --chat-id 7294961734 \
python /gfshome/MaskPrompt/src/main.py \
    --input_dataset 'advbench-custom' \
    --victim_model_name 'gpt-4o' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-mw' \
    --model_name 'gpt-4o' \
    --mode 7 \
    --defense ppl


# mp
knockknock telegram --token 7830241625:AAGyvxLxAUMYle4AgITGjHPObRG0FZxUPkM --chat-id 7294961734 \
python /gfshome/MaskPrompt/src/main.py \
    --input_dataset 'advbench-custom' \
    --victim_model_name 'gpt-4o' \
    --judge_model_name 'gpt-4o' \
    --ps 'wiki-text-infilling-mp' \
    --model_name 'gpt-4o' \
    --mode 7 \
    --defense ppl