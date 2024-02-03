import random
import json
import torch
from model import NeuralNet
from flask import Flask
from flask_restful import Api,Resource
from get_reply import reply

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

app = Flask(__name__)
api = Api(app)

class Update(Resource):
    def get(self,data):
        response = reply(str(data))
        return response

api.add_resource(Update,"/ask/<string:data>")

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0", port=5000)