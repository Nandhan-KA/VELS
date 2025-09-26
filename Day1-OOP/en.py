class bank:
    def __init__(self, Account_number, Name, Amount):
        self.Account_number =  Account_number
        self.Name=Name
        self.__Amount=Amount #private variable
            
        #getter method
    def balance(self):
        print("balance: ", self.__Amount)
    
    #setter method
    def deposit(self, amount):
        self.__Amount += amount
        #self.__Amount = self.__Amount + amount
        print("After deposit balance: ", self.__Amount)

c1=bank(1001, "Nandhan K", 10000000.0)
# c1.balance()
# c1.deposit(50000)
# c1.balance()
        
try:
    print(gyutytc)
except AttributeError:
    print("private variable cannot be accessed")
except Exception as e:
    print("Error: ", e)