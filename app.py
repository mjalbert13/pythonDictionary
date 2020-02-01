import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    w = word.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y  / N " % get_close_matches(w, data.keys())[0])
        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "n":
            return "Word does not exist. Please try again."
        else:
            return "Sorry I did not understand that word."
    else:
        return "The word does not exist. Please try again."

word = input("Enter a word: ")

print(translate(word))