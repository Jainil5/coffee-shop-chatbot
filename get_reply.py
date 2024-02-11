import random
import json
import torch
from model import NeuralNet
from spacy_utils import bag_of_words, tokenize
# from nltk_utils import bag_of_words, tokenize
from items_list import items 
from get_order import order
from train import data

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

# FILE = "data.pth"
# data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

# print(input_size,hidden_size,output_size,all_words,tags,model_state)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

names = list(items.keys())
prices = list(items.values())
text = ""

for item , price in items.items():
    text += f"""
    {item.upper()}  -----  {price} $. \n
    """
def reply(input):
    sentence = tokenize(input)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.50:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                response = random.choice(intent['responses'])
                if str(response).strip() == "asking_menu":
                    return f"{text}"
                elif str(response).strip() == "asking_prices":
                    return f"{text}"
                elif str(response).strip() == "giving_order":
                    response = order(input)
                    return response
                else:
                    return response
    else:
        return "Sorry! I did not understand this."