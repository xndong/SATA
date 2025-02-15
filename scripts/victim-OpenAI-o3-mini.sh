# SWQ (SATA-ELP)
declare -a pss=('swq-mask-sw' 'swq-mask-sp' 'swq-mask-mw' 'swq-mask-mp')

for ps in ${pss[@]};do
    python src/main.py \
        --input_dataset advbench-custom \
        --victim_model_name o3-mini \
        --judge_model_name gpt-4o \
        --ps ${ps} \
        --model_name gpt-4o \
        --mode 7 
done



# TextInfilling (SATA-MLM)
declare -a pss=('wiki-text-infilling-sw' 'wiki-text-infilling-sp' 'wiki-text-infilling-mw' 'wiki-text-infilling-mp')

for ps in ${pss[@]};do
    python src/main.py \
        --input_dataset advbench-custom \
        --victim_model_name o3-mini \
        --judge_model_name gpt-4o \
        --ps ${ps} \
        --model_name gpt-4o \
        --mode 7 
done

