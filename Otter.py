from Animal import Animal

class Otter(Animal):
    def __init__(self, name):
    
        super().__init__(name) 
        self.is_hungry = True
    def eat(self):

        if not self.is_hungry:
            return f"{self.name} is not hungry."
        self.is_hungry = False
        return f"{self.name} eats fish and is now full."

    def play(self):
        
        self.is_hungry = True
        return f"{self.name} is swimming with friends. Now {self.name} is hungry."