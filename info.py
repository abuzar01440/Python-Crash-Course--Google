# single underscore (_) = protected varibles
# Double underscore(__) = private variables ==> Under the hood, it change the name of a variable
# Either can be access within the class
class Information:
    def __init__(self, name_1:str, email:str, address_1): #instance attribute
        self.name_1 = name_1 #Instance attributes
        self._email = email # protected variable /////#Instance attributes
        self.address_1 = address_1 #Instance attributes

    def email_fix(self):
       return self._email.lower().strip()
    def name_fix(self):
        return self.name_1.lower().capitalize()

info = Information("saif", "Abz@gmail.com", "bhutta House")

print(50 * "_")
print(info.address_1)
print(50 * "_")
print(info._email)
print(50 * "_")
print(info.email_fix())
print(50 * "_")
print(info.name_fix())
print(50 * "_")
info.name_1= "FAIZ"
print(info.name_1)
print(50 * "_")
print(info.name_fix())
print(50 * "_")
print(50 * "_")
info._email = "saif@outlook.com" # remember we can change the value of a protected variable. but it is not convention
print(info._email)              # mostly developer uses it "_" as a convention



class User:
    def __init__(self,bio, home_numb):
        self.__bio = bio
        self.home_numb = home_numb

user = User("this is Ali Haider", 123)
print(user.__bio) # we can not access the __bio due to private variable ---> It through an error