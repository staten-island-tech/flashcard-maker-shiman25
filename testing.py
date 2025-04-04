""" 
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']

my_dict = dict(zip(keys, values))
print(my_dict) """
#########################################
""" words_data = []
def add_words():    
    keys= []
    values = []
    add = "yes"
    while add == "yes":
        word = input("the word ")
        keys.append(word)
        definition = input("the definition ")
        values.append(definition)
        add = input("continue? (yes or no) ")
    words = dict(zip(keys, values))
    words_data.append(words)  # Add the new word to the words_data
    print(words_data)
add_words() """

##########################################
""" class Word:
    def __init__(self, word, definition):
        self.word = word
        self.definition = definition
    def to_dict(self):
        return {"word": self.word, "definition": self.definition}

words = [
    Word("Blah", "This word is blah"),
    Word("r", "r") 
    
word = Word("Chevrolet", "A very expensive car brand")
words_data.append(word) """
############################################
""" def quizzie(streak,points):
    question = random.randint()
    answer = input("enter the definition")
# random digit -> find the corresponding word    
    if definition == answer:
        points = points*streak*2
        streak +=1
    else:
        print("incorrect")
        streak = 0  """
###########################################
""" import json
try:
    with open("flashCard.json", "r") as file:
        a = json.load(file)
except FileNotFoundError:
    a = []

b = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False
}
with open("flashCard.json", "w") as file:
    json.dump(b, file, indent=4)

print(a) """

import json

# Try to read the existing data from the file
try:
    with open("flashCard.json", "r") as file:
        content = file.read().strip()  # Read the file and strip any surrounding whitespace
        if content:  # If the file is not empty
            a = json.loads(content)  # Load the JSON data
        else:
            a = []  # If the file is empty, initialize an empty list
except (FileNotFoundError, json.JSONDecodeError):
    a = []  # If the file doesn't exist or is invalid, initialize an empty list

# New data to be added
b = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "is_student": False
}

# Append the new data to the existing data
a.append(b)

# Write the updated list back to the file
with open("flashCard.json", "w") as file:
    json.dump(a, file, indent=4)

# Print the updated contents of the file
print(a)