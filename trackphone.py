import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+60123751003")
phone_number2 = phonenumbers.parse("+60122370922")
phone_number3 = phonenumbers.parse("+60127589511")
phone_number4 = phonenumbers.parse("+60137789511")

print("\nPhone Numbers Location\n")
print(geocoder.description_for_number(phone_number1, "en"))
print(geocoder.description_for_number(phone_number2, "en"))
print(geocoder.description_for_number(phone_number3, "en"))
print(geocoder.description_for_number(phone_number4, "en"))

#Let's track the phone numbers