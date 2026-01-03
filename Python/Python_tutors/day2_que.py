vehicles = [
    {"make": "Toyota", "model": "Fortuner", "year": 2020, "price": 3200000, "mileage": 12, "engine_capacity": 2755, "category": "SUV"},
    {"make": "Toyota", "model": "Camry", "year": 2021, "price": 4100000, "mileage": 14, "engine_capacity": 2487, "category": "Sedan"},
    {"make": "Toyota", "model": "Hilux",  "year": 2022, "price": 3300000, "mileage": 10, "engine_capacity": 2755, "category": "Pickup"},
    {"make": "BMW",    "model": "M5",     "year": 2013, "price": 7500000, "mileage": 8,  "engine_capacity": 4395, "category": "Sports Sedan"},

    {"make": "BMW", "model": "X5", "year": 2018, "price": 6500000, "mileage": 11, "engine_capacity": 2998, "category": "SUV"},
    {"make": "BMW", "model": "3 Series", "year": 2020, "price": 4100000, "mileage": 16, "engine_capacity": 1998, "category": "Sedan"},
    {"make": "BMW", "model": "i8", "year": 2019, "price": 24000000, "mileage": 47, "engine_capacity": 1499, "category": "Hybrid Sports"},

    {"make": "Honda", "model": "City", "year": 2021, "price": 1200000, "mileage": 17, "engine_capacity": 1498, "category": "Sedan"},
    {"make": "Honda", "model": "Civic", "year": 2019, "price": 1800000, "mileage": 16, "engine_capacity": 1799, "category": "Sedan"},
    {"make": "Honda", "model": "CR-V", "year": 2020, "price": 2800000, "mileage": 14, "engine_capacity": 1997, "category": "SUV"},

    {"make": "Hyundai", "model": "Creta", "year": 2022, "price": 1600000, "mileage": 17, "engine_capacity": 1497, "category": "SUV"},
    {"make": "Hyundai", "model": "Verna", "year": 2021, "price": 1300000, "mileage": 18, "engine_capacity": 1497, "category": "Sedan"},
    {"make": "Hyundai", "model": "i20", "year": 2022, "price": 1000000, "mileage": 20, "engine_capacity": 1197, "category": "Hatchback"},

    {"make": "Ford", "model": "Endeavour", "year": 2019, "price": 3500000, "mileage": 10, "engine_capacity": 3198, "category": "SUV"},
    {"make": "Ford", "model": "Mustang", "year": 2018, "price": 7200000, "mileage": 7, "engine_capacity": 4951, "category": "Sports"},
    {"make": "Ford", "model": "EcoSport", "year": 2020, "price": 900000, "mileage": 15, "engine_capacity": 1497, "category": "Compact SUV"},

    {"make": "Maruti", "model": "Swift", "year": 2022, "price": 700000, "mileage": 21, "engine_capacity": 1197, "category": "Hatchback"},
    {"make": "Maruti", "model": "Baleno", "year": 2021, "price": 850000, "mileage": 20, "engine_capacity": 1197, "category": "Hatchback"},
    {"make": "Maruti", "model": "Brezza", "year": 2022, "price": 1100000, "mileage": 18, "engine_capacity": 1462, "category": "SUV"},

    {"make": "Kia", "model": "Seltos", "year": 2022, "price": 1700000, "mileage": 17, "engine_capacity": 1497, "category": "SUV"},
    {"make": "Kia", "model": "Sonet", "year": 2021, "price": 1200000, "mileage": 18, "engine_capacity": 1197, "category": "Compact SUV"}
]

# # 1. getting all vehicles info
# for vehicle in vehicles:
#     print(vehicle.items()) # each key-value pair 

# # 2. filter vehicles with respect to "make"
# Toyota_cars = [car for car in vehicles if car["make"]=="Toyota"]
# print("Following are the details of cars with Toyota: ", Toyota_cars)

# # 3. filter vehicles with respect to "year"
# year_manufactures = [car for car in vehicles if car["year"]==2021]
# print("Following are the details of cars manufactured in 2021: ", year_manufactures)

# # 4. Sorting using some key
# sorted_vehicles = sorted(vehicles, key= lambda x: x['year'], reverse= True)
# print([vehicle["year"] for vehicle in sorted_vehicles ])
