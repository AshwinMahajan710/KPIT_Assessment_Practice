# # Creating first class example
# class Product:
#     def __init__(self, id_, name_, price_):
#         self.pid = id_
#         self.name = name_
#         self.price = price_
    
#     def __repr__(self):
#         return f"Product ID: {self.pid}  Product Name: {self.name}  Price: {self.price}"


# prod = Product(101, "Pen", 10234)
# print(prod)

# # creating second class info 
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __repr__(self):
        return f"Product Name: {self.name}  Product Price: {self.price}  Quantity: {self.quantity}"
    
class Inventory:
    def __init__(self):
        self.products = []
    
    def __repr__(self):
        if not self.products:
            return "Inventory is empty"
        
        details = "Inventory Details:\n"
        for prod in self.products:
            details += repr(prod) + "\n"
        return details
    
    def search_Prods(self, prod_name: str):
        found = False
        for prod in self.products:
            if prod.name == prod_name:
                found = True
                break
        if found:
            print("Product found")
        else:
            print("Not found")
        
    # def update_onj(self, prod_name: str, new_name: str)

# operations tod do

        

