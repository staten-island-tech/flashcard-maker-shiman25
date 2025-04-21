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

with open('flashCard.json', 'r') as file:
    data = json.load(file)

third_item = data[0]
print(third_item)
