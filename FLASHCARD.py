import json

try:
    with open("flashCard.json", "r") as file:
        words_data = json.load(file)
except FileNotFoundError:
    words_data = []

class Teacher:
    def __init__(self, name):
        self.name = name
    def login(self):
        return f"you are logged in as {self.name}"
    def add_words(self):    
        keys= []
        values = []
        add = "yes"
        while add == "yes":
            word = input("the word ")
            keys.append(word)
            definition = input("the definition ")
            values.append(definition)
            add = input("continue? (yes or no) ")
        pair = dict(zip(keys, values))
        words_data.append(pair)  # Add the new word to the words_data
        

"""
class Student:
    def __init__(self, name):
        self.name = name
    def login(self):
        return f"you are logged in as {self.name}"
    def quiz(self):
        ...

"""
with open("flashCard.json", "w") as file:
    json.dump(words_data, file, indent=4) 

Sofia = Teacher("Sofia")
print(Sofia.login())
Sofia.add_words()
print(words_data)

