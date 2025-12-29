# Create a class EVCar with the following attributes

# - car_seat_count which is an integer (must be positive non-zero value)
# - car_price which is a non-zero, positive integer
# - car_battery_pack which is an instance of type BatteryPack (must NOT BE NULL)
# Create a class BatteryPack with the following attributes

# - battery_pack_serial_number which is a non-zero length string
# - battery_pack_type which is either LI_ION or NI_CAD
# Create an operations.py file with the following functionalities

# - Create a global dictionary of EvCar objects :
# - key should be:  car_reg_id which is a string starting with "MH" of length 9 or 10

# - A function add_new_ev_car_record which take required parameters and create an instance of type sensor. This instance must be added to the global dictionary
#     [Use a helper function to validate data received]

# - A function replace_battery_pack.It 
#     - receives an object of type BatteryPack and car_reg_id 
#     - updates the global dictionary for that car_reg_id by replacing existing battery_pack with newly received data
#     - Throws exceptions if received battery_pack data or car_reg_id is invalid/not-found

# - A function find_max_battery_capacity_car which returns the first EvCar instance whose battery_capacity is the highest.

# - A function to check if car instances have car_battery_pack with battery_capacity above 50 or not