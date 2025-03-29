class Cat:
    def __init__(self, name:str, breed:str, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print(f"The {self.name} cat breed is {self.breed} and its owner detail is {self.owner}")

class Owner:
    def __init__(self, name:str, address:str, phone_number:int):
        self.name = name
        self.address = address
        self.phone_number = phone_number
    


owner_1 =Owner("Saif", "lahore", 92323456789)
cat_1 = Cat(name="oscar", breed="persian", owner=owner_1)
print(66*"=")
print(cat_1.breed)
print(cat_1.owner.name)
print(cat_1.bark())
print(cat_1.owner.phone_number)
print(cat_1.owner.address)

print(66*"=")     