'''CLASS deep diving
    (1) ENCAPSULATION
    (2) INHERITENCE <
    (3) POLIMORPHISM <
'''
print("============================= INHERITENCE ===========================")
# PARENT > CHILD
# Parent only provides only public & protected properties(state + method) to children


class Animal:  # Parent
    description = "The class creates animals"

    def __init__(self, voice):
        self.voice = voice

    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):  # Child
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    def introduce(self):
        print(f" {self. name} says: {self.sound}-{self.sound}")

    def protect(self):
        print("Yes, can protect you!")


class Cat(Animal):  # Child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f" {self.name} says: {self.sound}-{self.sound}")

    def play(self):
        pass


class Fish(Animal):  # Child
    # state

    # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)

    # method
    def introduce(self):
        print(f"{self.name} says: {self. sound}-{self.sound}")

    def swim(self):
        print("Yes, can swim!")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "myeow", True)
fish = Fish("Nemo", "ZzZ", False)

dog.introduce()
cat.introduce()
fish.introduce()

print("----------------------------------------------")
dog.make_voice()
fish.make_voice()

print("---------------------------------------------")
print(Animal.description)
print(Dog.description)
