from Battery import Battery
from BatteryManagementSystem import BatteryManagementSystem
from CustomExceptions import InvalidDataTypeException
from enums import BatteryStatus, BatteryType

# 0.  Create dictionary for Battery objects
batteries = {}

# 1. Adding a new battery object to dictionary 
b1 = Battery(battery_id=101, battery_type=BatteryType.LI_ION, status=BatteryStatus.CHARGING, voltage=101, temperature= 101)
batteries[b1.battery_id] = b1

# Remove a Battery by ID
# Update Battery status:→ Change Enum status dynamically.
# Monitoring & Calculation
# Calculate total voltage of all batteries.
# Calculate average temperature.
# Find battery with max voltage
# Find battery with min temperature.
# Filter batteries above max temperature
# Filter batteries below min voltage.
# Generate alerts for abnormal conditions:→ Use lambda to check and append alerts.
# Create summary dictionary of battery voltages.
# Create list of battery types.
# Sort batteries by voltage
# Sort batteries by temperature descending
# Count batteries by status
# Predict charging completion time:→ Lambda based on voltage difference and charging rate.
# Generate historical voltage trend:→ Extract voltages from logs using [h['voltage'] for h in history].
# Check if all batteries are healthy (within limits)