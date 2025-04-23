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
        dictionary = json.load(file)

   
    random.shuffle(dictionary)
    for key in dictionary:
    w = []
    d = []

for d in dictionary:
    for k, v in d.items():
        keys.append(k)
        values.append(v)

print("Keys:", keys)
print("Values:", values)

