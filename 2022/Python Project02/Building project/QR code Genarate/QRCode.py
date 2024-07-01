import phonenumbers
from phonenumbers import timezone,geocoder,carrier
number=input("Enter phone number to get details +_ _: ")
num=phonenumbers.parse(number)
time=timezone.time_zones_for_number(number)
car=carrier.name_for_number(number,"en")
reg=geocoder.description_for_number(number,"en")

print(num)
print(time)
print(car)
print(reg)
