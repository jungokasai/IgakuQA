import string, mojimoji
import string, time
import numpy as np
from utils.tools import check_jsonls

def run_student(questions, meta_data):
    preds = []
    outputs = []
    for q_idx in range(len(questions)):
        question = questions[q_idx]
        meta = meta_data[q_idx]
        print(question['problem_id'])
        answer = find_majority(question, meta)
        preds.append(answer)
        outputs.append(answer)
    return preds, outputs

def find_majority(question, meta):
    assert question['problem_id'] == meta['problem_id']
    breakdown = np.array(list(map(float, meta['breakdown'])))
    nb_answers = len(question['answer'])
    top_k = list((-breakdown).argsort()[:nb_answers])
    alphabets = list(string.ascii_lowercase)
    outputs = ','.join([alphabets[idx] for idx in top_k])
    return outputs
