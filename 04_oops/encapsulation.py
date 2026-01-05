# encapsulation
# wrapping data and function into a single unit
# data hiding

class bankaccount:
    def __init__(self,name,balance):
        self.name=name                  #publlic
        self._balance=balance           #protected
        self.__private_balance=balance  #private

    # getter for protected
    def get_balance(self):
        return self._balance
    
    # getter for private
    def get_private_balance(self):
        return self.__private_balance
    
    # setter for protected
    def set_balance(self,new_balance):
        self._balance=new_balance

    # setter for private
    def set_private_balance(self,new_balance):
        self.__private_balance=new_balance
    
# object
acc=bankaccount("himanshu",2_000)

# outputs

# 1.public
print(acc.name)
# 2.protected
print(acc.get_balance())
# 3.private
print(acc.get_private_balance())

acc.set_balance(4_500)
acc.set_private_balance(6_500)

print(acc.get_balance())
print(acc.get_private_balance())
