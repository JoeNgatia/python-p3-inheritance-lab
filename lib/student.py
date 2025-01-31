from user import User  # Import User here as well

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []  # Start with an empty list for knowledge

    def learn(self, string):
        self.knowledge.append(string)  # Add the knowledge string to the list
