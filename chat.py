import random
import json
import torch
from model import NeuralNet
from get_reply import reply

bot_name = "Coffee Shop"
print("Let's chat! (type 'quit' to exit)")
while True:
    # sentence = "do you use credit cards?"
    sentence = input("You: ")
    if sentence == "quit":
        break
    else:
        response = reply(sentence)
        print(f"{bot_name}: {response}")    
    