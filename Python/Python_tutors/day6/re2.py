import re

text = "In 2025, Alex_T went to Room-42 at 10:30 AM to check sensor-data, but he noticed something strange! The device ID was 'A9B-77?' and the system displayed errors like E1, E12, and E123. Later, he wrote notes such as: temp=29C, humidity=70%, and status=OK. However, after 5 minutes, the sensor stopped responding... again! .error " 

# # 1 . mathcing the pattern --> match() only works if text is starting from the 'word' so below output will give 'none'
# pattern = r"went" --> match found at begining or not
# print(re.match(pattern, text))

# # 2. to search for pattern use 'search' not match()
# pattern = r"the" # will get only first occurance --> for all use 'findall'
# print(re.search(pattern, text))

# # 3. splitting the string
# pattern = r','
# print(re.split(pattern, text))

# # 4. finding one or more digit --> continuous
# pattern = r'\d+'
# print(re.findall(pattern=pattern, string=text))
    
# # 5. finding one or more --> alphanumeric
# pattern = r'\w+'
# print(re.findall(pattern=pattern, string=text))

# # 6. finding one or more non digit --> 
# pattern = r'\D+'  
# print(re.findall(pattern=pattern, string=text))

# # 7. finding one or more non alphanumeric 
# pattern = r'\W+'
# print(re.findall(pattern=pattern, string=text))

# # 8. splitiing based or more than one char
# pattern = r'[, -]'
# text = "1234-5678,3456 4567"
# print(re.split(pattern=pattern, string=text))

# # 9. splitiing based or more than one char
# pattern = r'[, -]'
# text = "1234-5678,3456 4567"
# print(re.split(pattern=pattern, string=text))

# # 10. validating vin is valid or not
# pattern = r'^[A-Z0-9]{17}$'
# vin = "WMI12345678901237"
# print(re.match(pattern=pattern, string=vin))
# start, end = re.match(pattern=pattern, string=vin).span()
# print(vin[start: end])

# # 11. matching the license plate pattern
# pattern = r"^[A-Z]{2}\s[0-9]{2}\s[A-Z]{2}\s[0-9]{4}$"
# license_plate = "MH 15 AZ 8906"
# print(re.match(pattern, license_plate))

# 12. matching the license plate pattern in the paragraph to find it --> it works
# pattern = r"[A-Z]{2}\s[0-9]{2}\s[A-Z]{2}\s[0-9]{4}"
# para = "During the routine inspection at the logistics hub, the supervisor noticed that one of the delivery vans had arrived earlier than scheduled. The driver, Rahul Verma, presented his identification documents along with his vehicle registration papers. His license number MH 14 DR 7296 and MH 15 DR 8906 was recorded in the daily logbook before he proceeded to the loading zone to collect the sealed shipment boxes. Everything appeared in order, and the team allowed him to continue without delay."
# print(re.findall(pattern, para))

# # 13. finding 'p' followed by 4 digits in error logs
# error_log = "P0300, P0301, P0302, P0300, P34, p567"  # Multiple DTCs
# pattern = r'P[0-9]{4}'
# print(re.findall(pattern, error_log))

# # 14. finding start and end for particular
# error_log = "P0300, P0301, P0302, P0300, P34, p567"  # Multiple DTCs
# pattern = r'P34'
# print(re.search(pattern, error_log).start())
# print(re.search(pattern, error_log).end())

# # 15. extracting all licese plate numbres
# text = "The vehicle's license plate is MH 12 AB 1234"
# pattern = r"\w{2}\s\d{2}\s\w{2}\s\d{4}"
# print(re.findall(pattern, text))

# # 16. validate string
# date_string = "2023-10-27"
# print(re.match(r"^\d{4}-\d{2}-\d{2}",date_string))

# # 17. extracting the email address
# log_content = "Report sent to user@example.com and support@kpit.com."
# pattern = r"[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z]{2,}"
# emails = re.findall(pattern, log_content)
# print(emails)

# strict validation by skipping some things
# vin = "1FVCP1U56XYZ123456"
# pattern = r"^[A-HJ-NPR-Z0-9]{17}$"  # Excludes I, O, Q
# if re.match(pattern, vin):
#     print("VIN is valid format")
# else:
#     print("VIN is invalid format")

# # 18. extracting speed and rpm
# can_message = "Speed: 65.2 km/h, RPM: 2500"
# pattern = r"(Speed: \d+\.\d\skm/h),\s*(RPM: \d+)"
# speed_rpm = re.findall(pattern,can_message)
# print(speed_rpm[0][0])
# print(speed_rpm[0][1])

# #19. # # Extract all part numbers (10 digits + 3 letters) from this list.
# text = "Ordered part number 1234567890ABC and another part 9876543210DEF."
# pattern = r"\d{10}\w{3}"
# print(re.findall(pattern, text))


# # 20. Parse key-value pairs from the data string (IMP not understanded)
# data_string = "EngineTemp=90.5,OilPressure=50,VehicleSpeed=80.2"
# pattern = r"([A-Za-z]+)=(\d+(?:\.\d+)?)"
# print(re.findall(pattern, data_string))

