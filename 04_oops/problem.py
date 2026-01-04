# problem
# design and create a store for products(name,price)
# track total no of products created
# create a static method to calculate the discount 


class store:
    count=0

    def __init__(self,name,price):
        self.name=name
        self.price=price
        store.count+=1 #here not self.count as in updating in class

    def getinfo(self):
        print(f"The price of {self.name} is RS{self.price}")

    @classmethod
    def get_count(cls):
        print(f"Total product in store is {cls.count}")

    @staticmethod
    def cal_discount(price,percentage):
        final_price=(f"final price={price-(price*percentage/100)}")
        return final_price
        
p=store("mi",10_000)
l=store("asus",80_000)

p.getinfo()
l.getinfo()
store.get_count()
print(store.cal_discount(p.price,10))
