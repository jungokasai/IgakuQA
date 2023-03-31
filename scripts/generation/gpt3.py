import openai, string, mojimoji
openai.api_key = ""
import string, time
import numpy as np
from utils.tools import check_jsonls

def run_gpt3(questions, model="text-davinci-003", prompt=None):
    preds = []
    outputs = []
    for q_idx in range(len(questions)):
        question = questions[q_idx]
        print(question['problem_id'])
        gpt3_input = create_input(prompt, question)
        done = False
        nb_trials = 0
        while not done:
            try:
                explanation, answer = gpt3_problem(gpt3_input, model)
                done = True
            except:
                print('\nfailed')
                time.sleep(5.0)
                nb_trials += 1
            if nb_trials == 3:
                explanation = 'NA'
                answer = 'NA'
                break
        preds.append(answer)
        outputs.append(explanation)
    return preds, outputs

def create_input(prompt, question):
    messages = []
    for example in prompt:
        messages.extend(dict2problem(example))
    messages.extend(dict2problem(question, False))
    messages = '\n'.join(messages)
    return messages

def dict2problem(dict_input, demo=True):
    problem = "問題: " + dict_input['problem_text']
    choices = dict_input['choices']
    answer = dict_input['answer']
    if len(choices) > 0:
        for choice, label in zip(choices, string.ascii_lowercase):
            problem = problem + '\n' + label + ': ' + choice
        problem = problem + "\n必ずa,b,c,d,eの中からちょうど{}個選んでください。".format(len(answer))
        problem = problem + "\n答え:"
    output = [problem]
    if not demo:
        return output
    output.append(",".join(answer))
    return output

def gpt3_problem(messages, model):
    output = openai.Completion.create(
                            model=model,
                            prompt=messages,
                            )
    answer = output["choices"][0]["text"].strip()
    pred = mojimoji.zen_to_han(answer).lower()
    return answer, pred
