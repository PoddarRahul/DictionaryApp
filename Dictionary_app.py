import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    matches = get_close_matches(word,data.keys())
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(matches)>0:
        for item in matches:
            yn = input("Did you mean %s? Enter Y for yes and N for no: " %item)
            if yn=="Y" or yn == "y":
                return data[item]
            elif yn=="N" or yn=="n":
                continue
            else:
                return ["Please enter a valid option next time"]
    else:
        return ["The word doesn't seem to exist in aour dataset. Please add it to the set. Thank you"]

do = "Y"

while(do != "N"):
    word = input("please enter a word: ")
    for w in translate(word):
        print(w)

    do = input("\nEnter Y if you want to search more else enter N: ")
    if(do == "N" or do == "n"):
        print("Thank You for searching with us. BYE BYE!!")
        break
