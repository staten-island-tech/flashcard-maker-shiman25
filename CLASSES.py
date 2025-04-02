class Merchant:
    def __init__(self, name, products):
        self.name = name
        self.products = products
    def sell(self,item):
        self.products.remove(item)
        print(self.products)

Rachel = Merchant("Rachel", ["Apples", "Oranges", "Human"])
Kammy = Merchant("Kammy", ["Penguins", "Whales", "Capybaras"])
print(Rachel.sell("Human"))
print(Kammy.sell("Capybaras"))

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"
    
class Student(User):
    def __init__(self, name, email, student_id):
        super().__init__(name,email) # Call the parent class constructor
        self.student_id = student_id
    
    def display_info(self):
        return f"User: {self.name}, Email: {self.email}, Student ID: {self.student_id}"

class Teacher(User):
    def __init__(self, name, email, subject):
        super().__init__(name,email)
        self.subject = subject

    def display_info(self):
        return f"User: {self.name}, Email: {self.email}, Subject: {self.subject}"
    
class Administrator(User):
    def __init__(self, name, email, role):
        super().__init__(name, email)
        self.role = role
    
    def display_info(self):
        return f"Administrator: {self.name}, Email: {self.email}, Role: {self.role}"
    
    def manage_system(self):
        return f"{self.name} ({self.role}) is managing the system"
 

 #######################################################################################

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_info(self):
        return f"User: {self.name}, Email: {self.email}"
    
class teacher(User):
    def __init__(self, name, email, subject):
        super().__init__(name,email)
        self.subject = subject

class Word:
    def __init__(self, word, definition):
        self.word = word
        self.definition = definition
    def to_dict(self):
        return {"word": self.word, "definition": self.definition}