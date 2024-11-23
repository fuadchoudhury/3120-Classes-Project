class Animal:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed 
      
    def describe(self):
        return f"{self.name} is {self.breed} breed of lion."
