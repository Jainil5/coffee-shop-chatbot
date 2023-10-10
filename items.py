import json

items = {
    "Black Coffee": "$10",
    "Cold Coffee": "$30",
    "Espresso":"$20",
    "Hot Choclate":"$20"
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

