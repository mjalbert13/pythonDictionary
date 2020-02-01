import json

data = json.load(open("data.json"))

def translate(word):
    w = word.lower()
    if w in data:
        return data[w]
    else:
        return "The word does not exist. Please try again."

word = input("Enter a word: ")

print(translate(word))