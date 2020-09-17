def sentencemaker(word):
    capitilize = word.capitalize()
    wordkey = ("How","When","Who","What")
    if capitilize.startswith(wordkey):
        return "{}?".format(capitilize)
    else:
        return "{}.".format(capitilize)

results = []
while True:
    word1 = input("enter word")
    if word1 == "\end":
        break
    else:
        results.append(sentencemaker(word1))

print("".join(results))
"""""
word =("how","who","when")
sen = "how are you "
if sen.startswith(word):
    sen.c
    print("question")
else:
    print("normal")
"""

## this is the trickiest logic ever that i completed it


