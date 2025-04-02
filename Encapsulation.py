# Encapsulation
#Encapsulation is one of the fundamental principles of object-oriented programming 
#that involves bundling data (attributes) and methods that operate 
# on the data within a single unit (class) while restricting direct access
#  to some of the object's components.

#=====================================================================

#In Python, encapsulation is implemented through:

#Access Modifiers
#Public attributes and methods (default):

#Accessible from anywhere
#No special naming convention
#Protected attributes and methods:

#Denoted by a single underscore prefix (_variable)
#Convention only (not enforced by Python)
#Signals "internal use only" to other developers
#Private attributes and methods:

#Denoted by double underscore prefix (__variable)
#Name mangling is applied (_ClassName__variable)
#Provides stronger access restriction (though not absolute)

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner        # Public attribute
        self._account_type = "Savings"  # Protected attribute
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.__balance  # Accessor method
     

bankaccount = BankAccount("Mehmat", 1000)
print(bankaccount.owner)  # Public attribute, accessible
print(bankaccount._account_type)  # Protected attribute, accessible but not recommended
print(bankaccount.get_balance())  # Accessing private attribute through method
#print(bankaccount.__balance)  # Raises AttributeError, private attribute not accessible directly
print(bankaccount._BankAccount__balance)  # Accessing private attribute through name mangling (not recommended)
# withdrawal
bankaccount.withdraw(200)  # Withdraw 200
print("The current Amount after withdraw ==>", bankaccount.get_balance())  # Check balance after withdrawal


# ======================================================================
# ----------------------------------------------------------------------

# Encapsulation in Python: Stock Portfolio Example
print("STOCK PORTFOLIO EXAMPLE")

class StockPortfolio:
    def __init__(self, owner_name):
        self.owner_name = owner_name  # Public attribute
        self._transaction_count = 0    # Protected attribute
        self.__holdings = {}           # Private: dictionary of stock:quantity
        self.__purchase_prices = {}    # Private: dictionary of stock:avg_price
        self.__portfolio_value = 0     # Private: calculated portfolio value
        
    def buy_stock(self, ticker, quantity, price_per_share):
        """Purchase stocks and update portfolio"""
        if quantity <= 0 or price_per_share <= 0:
            raise ValueError("Quantity and price must be positive")
            
        # Update transaction count
        self._transaction_count += 1
        
        # Update holdings
        if ticker in self.__holdings:
            # Calculate new average purchase price
            current_quantity = self.__holdings[ticker]
            current_value = current_quantity * self.__purchase_prices[ticker]
            new_value = quantity * price_per_share
            total_quantity = current_quantity + quantity
            
            self.__purchase_prices[ticker] = (current_value + new_value) / total_quantity
            self.__holdings[ticker] = total_quantity
        else:
            self.__holdings[ticker] = quantity
            self.__purchase_prices[ticker] = price_per_share
            
        # Update portfolio value
        self.__portfolio_value += quantity * price_per_share
        
        return self.__get_transaction_summary("BUY", ticker, quantity, price_per_share)
    
    def sell_stock(self, ticker, quantity, price_per_share):
        """Sell stocks and update portfolio"""
        if ticker not in self.__holdings:
            raise ValueError(f"You don't own any shares of {ticker}")
            
        if quantity <= 0 or price_per_share <= 0:
            raise ValueError("Quantity and price must be positive")
            
        if quantity > self.__holdings[ticker]:
            raise ValueError(f"You only own {self.__holdings[ticker]} shares of {ticker}")
            
        # Update transaction count
        self._transaction_count += 1
        
        # Calculate profit/loss
        purchase_price = self.__purchase_prices[ticker]
        profit_loss = (price_per_share - purchase_price) * quantity
        
        # Update holdings
        self.__holdings[ticker] -= quantity
        if self.__holdings[ticker] == 0:
            del self.__holdings[ticker]
            del self.__purchase_prices[ticker]
            
        # Update portfolio value
        self.__portfolio_value -= quantity * purchase_price
        
        return self.__get_transaction_summary("SELL", ticker, quantity, price_per_share, profit_loss)
    
    def __get_transaction_summary(self, action, ticker, quantity, price, profit_loss=None):
        """Private method to generate transaction summaries"""
        summary = f"{action}: {quantity} shares of {ticker} at ${price:.2f}"
        if profit_loss:
            status = "PROFIT" if profit_loss > 0 else "LOSS"
            summary += f" | {status}: ${abs(profit_loss):.2f}"
        return summary
    
    def get_portfolio_summary(self):
        """Return a summary of the portfolio"""
        if not self.__holdings:
            return "Portfolio is empty"
            
        summary = f"Portfolio for {self.owner_name}\n"
        summary += f"Total Value: ${self.__portfolio_value:.2f}\n"
        summary += f"Holdings:\n"
        
        for ticker, quantity in self.__holdings.items():
            value = quantity * self.__purchase_prices[ticker]
            summary += f"  {ticker}: {quantity} shares, Avg price: ${self.__purchase_prices[ticker]:.2f}, " \
                      f"Value: ${value:.2f}\n"
                      
        return summary
    
    @property
    def transaction_count(self):
        """Property to safely access transaction count"""
        return self._transaction_count
    
    @property
    def portfolio_value(self):
        """Property to safely access portfolio value"""
        return self.__portfolio_value
    # example of TICKER
# AAPL (Apple Inc.)
#MSFT (Microsoft Corporation)
#GOOGL (Alphabet Inc./Google)
#AMZN (Amazon.com Inc.)
##############################################################################

# The @property Decorator in Python
#The @property decorator in Python transforms a method into a getter
#  for a read-only attribute, creating a "pythonic" way to implement 
# getters and setters. It's an important tool for encapsulation.

# Example usage
portfolio = StockPortfolio("John Doe")
print(portfolio.buy_stock("AAPL", 10, 150))  # Buy 10 shares of AAPL at $150
print(portfolio.buy_stock("MSFT", 5, 200))   # Buy 5 shares of MSFT at $200
print(portfolio.sell_stock("AAPL", 5, 160))  # Sell 5 shares of AAPL at $160
print(portfolio.get_portfolio_summary())  # Get portfolio summary
print("Total transactions:", portfolio.transaction_count)  # Access protected attribute via property
print("Portfolio value:", portfolio.portfolio_value)  # Access private attribute via property
print(portfolio._transaction_count)  # Access protected attribute directly (not recommended)
print(portfolio._StockPortfolio__holdings)  # Access private attribute via name mangling (not recommended)
print(portfolio._StockPortfolio__purchase_prices)  # Access private attribute via name mangling (not recommended)
print(portfolio._StockPortfolio__portfolio_value)  # Access private attribute via name mangling (not recommended)
print(portfolio._StockPortfolio__get_transaction_summary("BUY", "AAPL", 10, 150))  # Access private method via name mangling (not recommended)
# ======================================================================


#------------------------------------------------------------------
# Python program to illustrate the use of
# @property decorator

# Defining class
class Portal:

	# Defining __init__ method
	def __init__(self):
		self.__name =''
	
	# Using @property decorator
	@property
	
	# Getter method
	def name(self):
		return self.__name
	
	# Setter method
	@name.setter
	def name(self, val):
		self.__name = val

	# Deleter method
	@name.deleter
	def name(self):
	    del self.__name

# Creating object
p = Portal()

# Setting name
p.name = 'GeeksforGeeks'

# Prints name
print (p.name)

# Deletes name
del p.name

# As name is deleted above this 
# will throw an error
# print (p.name)

class Portal:
    def __init__(self):
        self.__name = ''  # Private attribute (name mangling)
    
    @property              # Getter
    def name(self):
        return self.__name
    
    @name.setter          # Setter
    def name(self, val):
        self.__name = val

    @name.deleter         # Deleter
    def name(self):
        del self.__name
