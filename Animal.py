from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name
    
    def get_name(self):
        return self.name
    
    @abstractmethod
    def make_sound(self):
        pass
