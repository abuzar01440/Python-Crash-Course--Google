class Duck:
    def quack(self):
        return "Quack!"
    def walk(self):
        return "Waddle, waddle."

class Robot:
    def speak(self):
        return "Beep boop."
    def walk(self):
        return "Clank, clank."

class Human:
    def talk(self):
        return "Hello."

def make_it_walk_and_quack(animal):
    if hasattr(animal, 'walk') and hasattr(animal, 'quack'):
        print(f"It walks: {animal.walk()}")
        print(f"It quacks: {animal.quack()}")
    else:
        print("This object cannot walk and quack like a duck.")

my_duck = Duck()
my_robot = Robot()
my_human = Human()

print("--- Duck ---")
make_it_walk_and_quack(my_duck)

print("\n--- Robot ---")
make_it_walk_and_quack(my_robot) # Has walk but no quack

print("\n--- Human ---")
make_it_walk_and_quack(my_human) # Has neither

print("\n" + "--"*50 + "\n")

class OldAPI:
    def process(self, data):
        print(f"Processing with Old API: {data}")

class NewAPI:
    def handle(self, data):
        print(f"Handling with New API: {data}")
    def log_activity(self):
        print("Logging activity for New API.")

def perform_action(api_object, input_data):
    if hasattr(api_object, 'handle'):
        api_object.handle(input_data)
        if hasattr(api_object, 'log_activity'):
            api_object.log_activity()
    elif hasattr(api_object, 'process'):
        api_object.process(input_data)
    else:
        print("Unknown API object.")

old_api = OldAPI()
new_api = NewAPI()

perform_action(old_api, "item A")
perform_action(new_api, "item B")

################################################
print("\n" + "--"*50 + "\n")

#hasattr and duck typing
def check_duck_typing(obj):
    if hasattr(obj, 'quack') and hasattr(obj, 'walk'):
        print("This object can quack and walk like a duck.")
    else:
        print("This object does not confirm to the duck typing for a duck.")

check_duck_typing(my_duck)  # Should confirm duck typing
check_duck_typing(my_robot)  # Should not confirm duck typing

######################################################################

print("\n" + "--"*50 + "\n")

print("-- dog_behavior --")
print("\n" + "--"*50 + "\n")
# example of dog with duck typing hasattr

class Dog:
    def bark(self):
        return "Woof!"
    def walk(self):
        return "Trots along."
    def very_bark(self):
        return "WOOF WOOF! to much barking!"
    
bad_dog = Dog()


def dog_behavior(dog):
    if hasattr(dog, 'bark') and hasattr(dog, 'walk'):
        print(f"The dog barks: {dog.bark()}")
        print(f"The dog walks: {dog.walk()}")
    else:
        print("This object does not behave like a dog.")

dog_behavior(my_human)  # Should not behave like a dog
dog_behavior(bad_dog)  # Should behave like a dog
