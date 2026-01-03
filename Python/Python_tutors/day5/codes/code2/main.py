# main.py
from battery import Battery
from enums import BatteryType, BatteryStatus
from bms import BatteryManagementSystem

bms = BatteryManagementSystem()

# Create batteries
b1 = Battery(1, BatteryType.LI_ION, BatteryStatus.CHARGING, 3.7, 35)
b2 = Battery(2, BatteryType.NIMH, BatteryStatus.IDLE, 2.4, 40)
b3 = Battery(3, BatteryType.LEAD_ACID, BatteryStatus.DISCHARGING, 4.3, 65)

# Add them
bms.add_battery(b1)
bms.add_battery(b2)
bms.add_battery(b3)

print("Total Voltage:", bms.calculate_total_voltage())
print("Average Temperature:", bms.calculate_average_temperature())
print("Max Voltage Battery:", bms.battery_with_max_voltage())
print("Min Temp Battery:", bms.battery_with_min_temperature())
print("Alerts:", bms.generate_alerts())
print("Summary Voltages:", bms.summary_voltages())
print("Battery Types:", bms.list_battery_types())
print("Sorted by Voltage:", bms.sort_by_voltage())
print("Sorted by Temp Desc:", bms.sort_by_temperature_desc())
print("Count by Status:", bms.count_by_status())
print("Charging Time Prediction:", bms.predict_charging_time(1))
print("All Batteries Healthy?", bms.all_batteries_healthy())
