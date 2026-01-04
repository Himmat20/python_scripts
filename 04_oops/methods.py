# instance 
class laptop:
    storage_type="ssd"

    def __init__(self,RAM,storage):
        self.RAM=RAM  #instance method 
        self.storage=storage
    def get_info(self):
        print(f"laptop has {self.RAM} and storage of {self.storage} {self.storage_type}")

l1=laptop("16gb","512gb")
l2=laptop("8gb","256gb")

# 
# l1.get_info()

# instance method 
# compulsory parameter is self
# they can access the class and instance attribute

# class
class mahindra:
    company="mahindra motors"

    def __init__(self,c_name,mf_year):
        self.c_name=c_name
        self.mf_year=mf_year
    
    
    @classmethod
    def show_company_name(cls):
        print(f"company ={cls.company}")

        
    def get_info(self):
        print(f"The {self.company} {self.c_name} is made in year:{self.mf_year}")


c1=mahindra("thar",2025)
c2=mahindra("scorpio",2026)

# mahindra.show_company_name()
# c1.get_info()
# c2.get_info()

# 3.static method
class tata:
    company="tata"

    def __init__(self,model,year):
        self.model=model
        self.year=year

    @classmethod
    def show_company(cls):
        print (f"company = The {cls.company} Motors")

    def get_val(self):
        print(f"{self.model} is manufactured in the year :{self.year}")

    @staticmethod
    def cal_discount(price,discount):
        final_price=price-(discount*price/100)
        return (f"final price={final_price}")


car_1=tata("harrier",2019)
car_2=tata("sierra",2025)

car_1.get_val()
car_2.get_val()
tata.show_company()
print(car_1.cal_discount(1_30_000,15))