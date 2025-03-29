# Accessing and modify the data
# Property decorator & ===> getter method

class mobile:
    def __init__(self, model:str, ram:float, memory:float):
        self.model = model
        self._ram = ram # protected
        self.memory = memory
    """
    Here, we will get RAM information from the @property decorator not from protected variable
    """

    @property
    def ram(self):
        print("RAM info accessed in GBs")
        return self._ram
    def check_memory(self):
        print("Checking Memory...")
        if type(self.memory) is type(self._ram):
                print("OKAY")
        else:
            print("Memory is in Str format")

    
cell= mobile(model="spark 7 pro", ram=7.9, memory="zar")
print(cell.ram)

print(cell.check_memory())
        


