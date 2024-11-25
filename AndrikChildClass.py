#Andrik Child Class
from Animal import Animal 
class Rabbit(Animal):
    def __init__(self, name, fur_color, eye_color, diet):  
        super().__init__(name)  
        self.fur_color = fur_color
        self.eye_color = eye_color
        self.diet = diet

    def make_sound(self):  
        return "Sniff sniff!"

    def getrabbit(self): 
        return f"{self.name} the Rabbit has {self.fur_color} fur, has {self.eye_color} eyes, and it is a {self.diet}."


rabbit = Rabbit(name="Hooper", fur_color="Brown", eye_color="Red", diet="Herbivore")


print(rabbit.get_name())  
print(rabbit.make_sound())  
print(rabbit.getrabbit())  