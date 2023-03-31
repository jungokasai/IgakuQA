# Igaku QA Scripts
All API keys are removed. You need to get your key for GPT-3 or ChatGPT/GPT-4 if you want to run them.

## Prediction
We provide five baselines provided in our paper. Run:
```bash
python baseline_main.py --in-file ../data/2018/112-A.jsonl --config chatgpt
python baseline_main.py --in-file ../data/2018/112-A.jsonl --config gpt4
python baseline_main.py --in-file ../data/2018/112-A.jsonl --config gpt3
python baseline_main.py --in-file ../data/2018/112-A_translate.jsonl --config chatgpt-en --prompt-file prompts/prompt_translate.jsonl 
python baseline_main.py --in-file ../data/2018/112-A.jsonl --student-majority
```
This will output prediction jsonl files in `../baseline_results/`. Replace the `--in-file` argument with your questions.

## Evaluation
```bash
python evaluate_main.py --gold-file ../data/2018/112-A.jsonl --pred-file ../baseline_results/2018/112-A_chatgpt.jsonl
```
