import json
from difflib import get_close_matches
data = json.load(open("data.json"))
def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(w, data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."
word = input("Enter word: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

"""
so we understand what is the process going on in steps 

1. we import json here which is in the form of list 
2. we create a function which is provide us the meaning of the the giving words
3. we convert the data in lower as user can be given word in any terms 
4. but word.title is also given as some word is always capital in first letter  like "Delhi" 
5. and word.upper is also given as some word is always capital like "USA"
6.The important part of the dictionary is sometime user can give the wrong spell word so we want it send the best match 
to the user if he think it is correct then he can select with y and otherwise n
7.the output is come in the form of list
8. so we need to convert it into the string and for is the way to collect is individually.
thats it 

thank you 

"""
