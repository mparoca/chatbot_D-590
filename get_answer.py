from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import wikipedia as wiki
import torch

model_path = 'deepset/roberta-base-squad2' #Using bert-base-cased-squad2 temporarily because custom roberta model is too lage for github feel free to use 'models/roberta-custom' in local after training
#model_path = 'models/roberta-custom'
model = AutoModelForQuestionAnswering.from_pretrained(model_path, return_dict=False)
tokenizer = AutoTokenizer.from_pretrained(model_path)


def get_answer(question):
    results = wiki.search(question)
    page = wiki.page(results[0])
    text = page.content
    context = text[:model.config.max_position_embeddings]
    inputs = tokenizer.encode_plus(question, context, return_tensors="pt") 
    answer_start_scores, answer_end_scores = model(**inputs)
    answer_start = torch.argmax(answer_start_scores)  # get the most likely beginning of answer with the argmax of the score
    answer_end = torch.argmax(answer_end_scores) + 1  # get the most likely end of answer with the argmax of the score
    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][answer_start:answer_end]))
    return answer


#print(get_answer("what does the president of the usa do?"))
