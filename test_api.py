import requests

base = "http://127.0.0.1:5000/ask/"

res = requests.get(base+"hi, how are you")
print(res.text)