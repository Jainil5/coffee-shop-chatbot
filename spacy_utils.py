import spacy
import numpy as np
import subprocess

# subprocess.run("python -m spacy download en_core_web_sm")

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def tokenize(sentence):
    doc = nlp(sentence)
    return [token.text for token in doc]

def lemmatize(word):
    lemma = nlp(word)[0].lemma_
    return lemma

def bag_of_words(tokenized_sentence, all_words):
    lemmatized_sentence = [lemmatize(w) for w in tokenized_sentence]

    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in lemmatized_sentence:
            bag[idx] = 1

    return bag


# print(tokenize("Hello this is running like a bull."))
