import phonenumbers
from phonenumbers import geocoder
ph1=phonenumbers.parse("+917378125935")
ph3=phonenumbers.parse("+919793872932")
ph2=phonenumbers.parse("+12136574429")

print("\nPhone Numbers Location:\n")
print(geocoder.description_for_number(ph1,"en"))
print(geocoder.description_for_number(ph2,"en"))
print(geocoder.description_for_number(ph3,"en"))