class PetAnimal:
    def __init__(self,breed,colour,size):
        self.breed=breed
        self.colour=colour
        self.size=size
        self.function()
    def __str__(self):
        return (
            f"Your pet breed is {self.breed}\n"
            f"Your pet colour is {self.colour}\n"
            f"Your pet size is {self.size}"
        )
    def function(self):
        animal=input("enter your pet  animal name: ")
        self.bark(animal)
    def bark(self,animal):
        if animal=="dog":
           print("dog bark like wo wo wowo")
        elif animal=="cat":
            print("cat sound like meow meow")
        else:
            print("no pet and sound define for this pet")

colour=input("enter your pet colour: ")
size=input("enter your pet size: ")
breed=input("enter the breed: ")
pet1=PetAnimal(breed,colour,size)
print(pet1)