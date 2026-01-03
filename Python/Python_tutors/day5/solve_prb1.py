# class Vehicle:
    
#     # // static variable
#     vehicle_count = 0

#     def __init__(self, brand: str, model: str, year: int) -> None:
#         self.brand = brand
#         self.model = model
#         self.year = year
#         Vehicle.vehicle_count += 1
    
#     # writing the static method
#     @classmethod
#     def get_brand_model_name(cls, fullname: str) -> str:
#         brand, model =  fullname.split('-')
#         return brand,model

#     @classmethod 
#     def total_vehicle_count(cls)->int:
#         return cls.vehicle_count

# # creating objects
# v1: Vehicle = Vehicle("Toyota","Supra",12345678)
# v2: Vehicle = Vehicle("Toyota","Hilux",2345678)

# # using the class static method to get brand and model name from string
# brand, model = Vehicle.get_brand_model_name("Toyota-Fortuner")
# print("Brand: ",brand," Model: ",model)

# # Printing the total cars created --> both methods are valid
# print("Total cars count: ",Vehicle.total_vehicle_count())
# print("Total cars count: ",Vehicle.vehicle_count)

#  ===============================================================================================================================


# class Bank:
#     yearly_intrest: float = 3.0

#     def __init__(self, first_name: str, last_name: str, bank_balance: float):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.bank_balance = bank_balance
    
#     def get_intrest_amount(self)->float:
#         return (Bank.yearly_intrest)*(self.bank_balance)/100.0

#     @classmethod
#     def get_intrest_rate(cls):
#         return cls.yearly_intrest
    
#     def display_details(self)->str:
#         return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nBank Balance: {self.bank_balance}\nIntrest for first Year: {self.get_intrest_amount()}"

# b1 : Bank = Bank("Ashwin","Mahajan", 10000)
# print(b1.display_details())
# print("Yearly Intrest Rate: ",Bank.get_intrest_rate())

# ================================================================================================================================

# class Car:
#     company_name = "AutoMobiles Ltd"   # Class variable
#     car_count = 0                      
 
#     def __init__(self, model, year):
#         self.model = model             # Instance variable
#         self.year = year               
#         Car.car_count += 1            
 
#     def show_details(self):
#         print(f"Model: {self.model}, Year: {self.year}, Company: {Car.company_name}")
 
#     @classmethod
#     def change_company(cls, new_name):
#         cls.company_name = new_name
#         print(f"Company name changed to: {cls.company_name}")
 
#     @classmethod
#     def get_car_count(cls):
#         return cls.car_count
 
 
# # Creating objects
# c1 = Car("Sedan X", 2022)
# c2 = Car("SUV Pro", 2023)
 
# c1.show_details()
# c2.show_details()
 
 
# Car.change_company("Global Auto Corp")
 
# c1.show_details()
# c2.show_details()
 
# print("Total Cars Manufactured:", Car.get_car_count())

# ================================================================================================================================

class Operations:
    
    # add method
    @staticmethod
    def add(x,y):
        return x+y
    
    # multiply method
    @staticmethod
    def multiply(x,y):
        return x*y
    
    # divide method
    @staticmethod
    def divide(x,y):
        return x//y

obj1: Operations = Operations()
print(Operations.add(1,2))
print(Operations.multiply(1,2))
print(Operations.divide(1,2))