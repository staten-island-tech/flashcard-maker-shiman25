import json

# Attempt to load existing data from the file
try:
    with open("flashCard.json", "r") as file:
        a = json.load(file)  # Directly load JSON data from the file
except (FileNotFoundError, json.JSONDecodeError):
    a = []  # Initialize an empty list if file is not found or the content is invalid

# New data to be added
b = {
    "name": "Elise",
    "age": 19,
    "random": "Yes",
    "isStudent": True
}

class C:
    def __init__(self, name):
        self.name = name
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
        return pair
        
Sofia = C("Sofia")
result = Sofia.add_words()

if result:
    a.append(result)

with open("flashCard.json", "w") as file:
    json.dump(a, file, indent=2)