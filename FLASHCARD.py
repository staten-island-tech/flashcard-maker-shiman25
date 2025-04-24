import random
import json
try:
    with open("flashCard.json", "r") as file:
        words_data = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    words_data = []

class Teacher:
    def __init__(self, name):
        self.name = name
    def login(self):
        return f"you are logged in as {self.name}"
    def add_words(self):    
        keys= []
        values = []
        add = "y"
        while add == "y":
            word = input("the word ")
            keys.append(word)
            definition = input("the definition ")
            values.append(definition)
            add = input("continue? (type y or n) ")
        pair = dict(zip(keys, values))
        return pair

Login = input("Student Mode or Teacher Mode? (type t or s): ")
if Login == "t":
    teach = Teacher("teach")
    print(teach.login())

    new_words = teach.add_words()
    words_data.append(new_words)

    with open("flashCard.json", "w") as file:
        json.dump(words_data, file, indent=4) 

if Login == "s":
    print("start quiz!")

    with open("flashCard.json", "r") as file:
        theCards = json.load(file)
    #random.shuffle(theCards)

print(theCards)
w = []
d = []
streak = 0
for i in theCards:
    for key, value in i.items():
        w.append(key)
        d.append(value)

combined = list(zip(w, d))
print(combined)

""" for word in w:
    print(word)
    answer = input("Definition? ")
    k = d[0]
    print("the correct answer is: ", k)
        
    
    if answer == k:
        print("Correct!")
        streak +=1
        point +=1
        if streak == 5:
            streak == 0
            point += 5

    else:
        print("Incorrect!")
        streak == 0  """
