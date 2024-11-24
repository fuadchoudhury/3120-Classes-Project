from abc import ABC, abstractmethod
#Parent Class
class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    @abstractmethod
    def make_sound(self):
        pass
#Child Class
class Lion(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def make_sound(self):
        return "ROAR!"
    def describe(self):
        return f"{self.name} is {self.breed} breed of lion and says {self.make_sound()}."

lions = [
    Lion(name="Mufasa", breed="Asiatic Lion"),
    Lion(name="Scar", breed="Barbary Lion"),
    Lion(name="Simba", breed="African Lion"),
    Lion(name="Nala", breed="Cape Lion"),
]

if __name__ == "__main__":
    for lion in lions:
        print(lion.describe())