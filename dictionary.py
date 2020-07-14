import json
from spellchecker import SpellChecker
from difflib import get_close_matches



#print(dict)
#print(len(dict))

dict = json.load(open("data.json"))



word = input("Enter the word to be searched :")



if word.lower() in dict:
    if type(dict[word.lower()]) == list:
        for elem in dict[word.lower()]:
            print(elem)
elif word.title() in dict:
    if type(dict[word.title()]) == list:
        for elem in dict[word.title()]:
            print(elem)
elif word.upper() in dict:
    if type(dict[word.upper()]) == list:
        for elem in dict[word.upper()]:
            print(elem)

else:
    closest = get_close_matches(word,dict.keys())
    print("COULDN'T FIND WORD: " + word)
    print("TRY THESE WORDS: ")
    if type(closest) == list:
        for elem in closest:

            print(elem)
    #print("word does not exist")
