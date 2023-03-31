import openai, string, mojimoji
openai.api_key = ""
import string, time
from utils.tools import check_jsonls
import threading

def run_chatgpt(questions, model="gpt-3.5-turbo", prompt=None):
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
                if answer is None:
                    done = False
                    print('\nfailed')
                else:
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
    messages = [{"role": "system", "content": "医師国家試験を解きます。"}]
    for example in prompt:
        messages.extend(dict2problem(example))
    messages.extend(dict2problem(question, False))
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
    output = [{"role": "user", "content": problem}]
    if not demo:
        return output
    output.append({"role": "assistant", "content": ",".join(answer)})
    return output

def chatgpt_problem(messages, model):
    t = threading.Thread(target=run_api, args=(model, messages,))
    t.start()
    max_time = 30
    while t.is_alive() and max_time > 0:
        time.sleep(0.1)  # check every 0.1 seconds
        max_time -= 0.1
    if t.is_alive():
        # Thread is still running after maximum time limit
        # We need to stop it and exit the program
        print("Maximum time limit exceeded. Exiting program...")
        t._stop()
        return None, None
    answer = output['choices'][0]['message']['content']
    pred = mojimoji.zen_to_han(answer).lower()
    t._stop()
    return pred

def run_api(model, messages):
    global output
    output = openai.ChatCompletion.create(
      model=model,
      messages=messages,
    )
