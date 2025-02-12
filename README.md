
## Introduction of SATA
### SATA-MLM
![](assets/method-v2-part1-underline-resize.png)
### SATA-ELP
![](assets/method-v2-part2-resize.png) 

## Before Your Running
### 1. Create Environment for the Experiments

Create a new environment and activate it
```bash
# create a new environment
conda env create -f environment-llm-safety.yml
# activate the environment
source activate llm-safety 
# alternatively, use the following command to activate the environment
conda activate llm-safety
```
or only install the required packages without creating a new environment
```bash
# ignore the dependencies
pip install --no-deps -r requirements.txt
# alternatively, install the dependencies
pip install -r requirements.txt
```
### 2. Prepare API Keys or Service Endpoint for the Experiments
Make sure setup your API keys or service endpoint in `utility/model.py` before running experiments.
- OpenAI API key
- Claude API key
- API key in cloud services: DeepInfra or SiliconFlow
- Azure OpenAI endpoint and API key (optional)

We leave the API keys or service endpint as a placeholder in the code. You need to replace them with your own API keys or service endpoint. The place holder is like `PLACEHOLDER_FOR_YOUR_API_KEY` or `PLACEHOLDER_FOR_YOUR_AZURE_OPENAI_ENDPOINT`.


## Run SATA
### Run Jailbreak Inference and Evaluation
You can run a single experiment with the following command (You can change the `--victim_model_name`, `--ps` or any arguments. More details please refer to `main.py` and `utility/argsparse.py`):
```bash
# SATA-ELP
python src/main.py --input_dataset advbench-custom --victim_model_name gpt-3.5-turbo --judge_model_name gpt-4o --ps swq-mask-sw --mode 7
# SATA-MLM
python src/main.py --input_dataset advbench-custom --victim_model_name gpt-3.5-turbo --judge_model_name gpt-4o --ps wiki-text-infilling-sw --mode 7
```
or if you want to quickly re-produce our experimental results, just run a batch of experiments with our prepared scripts:
```bash
# SATA-ELP
bash scripts/victim-gpt-3.5-turbo.sh
# SATA-MLM
bash scripts/victim-gpt-3.5-turbo-TextInfilling.sh
```
You can find many scripts in the `scripts` directory.

### Run Jailbreak Inference Only
- You should change the bash command argument from `--mode 7` to `--mode 4`
```bash
# SATA-ELP
python src/main.py --input_dataset advbench-custom --victim_model_name gpt-3.5-turbo --judge_model_name gpt-4o --ps swq-mask-sw --mode 4
# SATA-MLM
python src/main.py --input_dataset advbench-custom --victim_model_name gpt-3.5-turbo --judge_model_name gpt-4o --ps wiki-text-infilling-sw --mode 4
```

### Run Jailbreak Evaluation Only
- For GPT evaluation, you should change the bash command argument from `--mode 7` to `--mode 1`
- For sub-string evaluation, you should change the bash command argument from `--mode 7` to `--mode 2`
- For both GPT evaluation and sub-string evaluation, you should change the bash command argument from `--mode 7` to `--mode 3`
- Forcelly re-evaluate by GPT, you should change the bash command argument from to `--mode 8`
```bash
# remember to add `--exp_id` argument
python src/main.py --input_dataset advbench-custom --victim_model_name gpt-3.5-turbo --judge_model_name gpt-4o --ps swq-mask-sw --mode 3 --exp_id PASTE_YOUR_expID
```

### Run SATA with Jailbreak Defense
You should add a bash command argument `--defense`, e.g. `--defense ppl`, `--defense rpo`.
For example, you can run a single inference experiment:
```bash
# SATA-ELP
python src/main.py --input_dataset advbench-custom --victim_model_name gpt-3.5-turbo --judge_model_name gpt-4o --ps swq-mask-sw --defense ppl --mode 7
# SATA-MLM
python src/main.py --input_dataset advbench-custom --victim_model_name gpt-3.5-turbo --judge_model_name gpt-4o --ps wiki-text-infilling-sw --defense ppl --mode 7
```
or if you want to quickly re-produce our experimental results with defense, just run a batch of experiments with our prepared scripts:
```bash
# SATA-ELP
bash scripts/defense-ppl/victim-llama3-70b.sh
# SATA-MLM
bash scripts/defense-ppl/victim-llama3-70b-TextInfilling.sh
```

### Ensemble the Results of SATA
We provide jupyter notebooks for you to ensemble the results of SATA with different `--ps`. You can find the notebook in the `src` directory.

## Acknowledgement
This repository is based on the ArtPrompt repository. We thank the authors for their great work.
