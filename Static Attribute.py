#Static Attribute
""""Static attribute also called class attribute"""
""""It is a Variable that is shared by all inatances of a class...
    It always defined inside the class  defined but outside of any instance method...
    It can  accessed via the class name or via any instance of the class"""
# Benefits
"""
    *   Memory Efficiency
    *   Global Access
    *   Constant Value
    *   Cache: Static attribute can be used as a cashe to store values that are expensive to compute"""

class User:
    count_user = 0 #static attribute
    def __init__(self, username:str, email:str): 
        self.username = username #Instance attributes
        self.email = email #Instance attributes
        User.count_user +=1
        
    def display_user(self):
        print(f"Username {self.username} and Email Address {self.email}")


user_1 = User(username="ALI", email="alihaidarbhutta01@gmail.com")
user_2 = User(username="ALI Bhutta", email="alihaidarbhutta02@gmail.com")
user_3 = User(username="ALI Haidar Moshin", email="alihaidarbhutta03@gmail.com")
user_4 = User(username= "Soniya Haidar", email="soniyalihaidar004@gmail.com")

print(User.count_user)

#Output should be 4


""" The staticmethod decorator is used to define a static method within a class
* Noted that Static method don't receive the self or cls parameters 
    """

class Bankaccount:
    minimum_balance = 100
    def __init__(self, name:str, balance:float = 0):
        self.name = name
        self.balance = balance

    def _is_valid_amount(self, amount:float):
        return amount>0
    def deposit(self, amount:float):
        if self._is_valid_amount(amount) >0:
            self._balance +=amount #protected variable
            self.__log_transection_type("Deposit", amount) 
            
        else:
            print("Recheck Enter AMOUNT maybe it is negative")

    def __log_transection_type(self, transection_type:str, amount:float): #private
         print(f'Transectiont Type {transection_type}, Amount {amount}, and current new balance {self._balance}')

    @staticmethod
    def is_valid_interestRate(rate:float):
        return 0 <=rate<=0

customer = Bankaccount("Ali Haidar Bhutta", 399)
customer.deposit(amount=300)

print(customer.is_valid_interestRate(12))