import json

items = {
    "americano": "6",
    "cappucino": "5",
    "flat white":"7",
    "caffe latte":"7",
    "frappe": "10",
    "iced latte": "20",
    "iced mocha":"20",
    "iced coffee":"30",
    "black coffee":"10",
    "cold coffee":"20"
    }

def get_sentences():
    items_list = list(items.keys())
    sentences = []
    if len(items_list)!= 0:
        for item in items_list:
            sentence = f"Order me a {item}."
            sentences.append(sentence)
            sentence = f"I want a {item}." 
            sentences.append(sentence)
            sentence = f"Give me a {item}." 
            sentences.append(sentence)
            sentence = f"Bring me a {item}." 
            sentences.append(sentence)
            sentence = f"Give me a {item}." 
            sentences.append(sentence)
            sentence = f"Can you order me a {item}?" 
            sentences.append(sentence)
            sentence = f"Can you give me a {item}?" 
            sentences.append(sentence)
    
    return sentences  

# print(get_sentences())

