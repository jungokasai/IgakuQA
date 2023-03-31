import openai, string, mojimoji
openai.api_key = ""
import string, time
import numpy as np
from utils.tools import check_jsonls

def run_chatgpt_en(questions, model="gpt-3.5-turbo", prompt=None):
    preds = []
    outputs = []
    for q_idx in range(len(questions)):
        question = questions[q_idx]
        print(question['problem_id'])
        chatgpt_input = create_input(prompt, question)
        done = False
        nb_trials = 0
        while not done:
            try:
                answer = chatgpt_problem(chatgpt_input, model)
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
        outputs.append(answer)
    return preds, outputs

def create_input(prompt, question):
    messages = [{"role": "system", "content": "Let's try Japan's medical license exam."}]
    for example in prompt:
        messages.extend(dict2problem(example))
    messages.extend(dict2problem(question, False))
    return messages

def dict2problem(dict_input, demo=True):
    problem = "Problem: " + dict_input['problem_text_en']
    choices = dict_input['choices_en']
    answer = dict_input['answer']
    if len(choices) > 0:
        for choice, label in zip(choices, string.ascii_lowercase):
            problem = problem + '\n' + label + ': ' + choice
        problem = problem + "\nChoose exactly {} correct choice(s) from a, b, c, d, e.".format(len(answer))
        problem = problem + "\nAnswer:"
    output = [{"role": "user", "content": problem}]
    if not demo:
        return output
    output.append({"role": "assistant", "content": ",".join(answer)})
    return output

def chatgpt_problem(messages, model):
    print(messages)
    output = openai.ChatCompletion.create(
      model=model,
      messages=messages,
    )
    answer = output['choices'][0]['message']['content']
    pred = mojimoji.zen_to_han(answer).lower()
    return pred
