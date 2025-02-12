# sw
knockknock telegram --token 7830241625:AAGyvxLxAUMYle4AgITGjHPObRG0FZxUPkM --chat-id 7294961734 \
python src/main.py \
    --input_dataset advbench-custom \
    --victim_model_name llama3-api-70b \
    --judge_model_name gpt-4o \
    --ps swq-mask-sw \
    --model_name gpt-4o \
    --mode 7 \
    --temperature 0.6 \
    --defense retok


# sp
knockknock telegram --token 7830241625:AAGyvxLxAUMYle4AgITGjHPObRG0FZxUPkM --chat-id 7294961734 \
python src/main.py \
    --input_dataset advbench-custom \
    --victim_model_name llama3-api-70b \
    --judge_model_name gpt-4o \
    --ps swq-mask-sp \
    --model_name gpt-4o \
    --mode 7 \
    --temperature 0.6 \
    --defense retok


# mw
knockknock telegram --token 7830241625:AAGyvxLxAUMYle4AgITGjHPObRG0FZxUPkM --chat-id 7294961734 \
python src/main.py \
    --input_dataset advbench-custom \
    --victim_model_name llama3-api-70b \
    --judge_model_name gpt-4o \
    --ps swq-mask-mw \
    --model_name gpt-4o \
    --mode 7 \
    --temperature 0.6 \
    --defense retok


# mp
knockknock telegram --token 7830241625:AAGyvxLxAUMYle4AgITGjHPObRG0FZxUPkM --chat-id 7294961734 \
python src/main.py \
    --input_dataset advbench-custom \
    --victim_model_name llama3-api-70b \
    --judge_model_name gpt-4o \
    --ps swq-mask-mp \
    --model_name gpt-4o \
    --mode 7 \
    --temperature 0.6 \
    --defense retok
