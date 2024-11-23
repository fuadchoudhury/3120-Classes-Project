from main_repository.animal import Animal
class Lion(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed    
    def speak(self):
        return f"{self.name} scream ROAR!" 
