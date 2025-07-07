import datetime


name = "Hasan"
surname = "Kacar"
fullName = name + " " + surname
gender = True
identityNumber = 15768541203
birthdate = datetime.datetime(1999, 1, 1)
age = 26
address = '1111 sokak no.8 d.2 Merkezefendi/Denizli'


print("Name : ", name)
print("Surname : ", surname)
print("Full Name : ", fullName)
print("Gender : ", "Male" if gender else "Female")
print("Identity Number : ", identityNumber)
print("Birthdate : ", birthdate)
print("Age : ", age)
print("Address : ", address)




print("\n*************************************\n")

order1 = 110
order2 = 1100.5
order3 = 356.95

totalOrderAmount = order1 + order2 + order3
print("Total Order Amount : ", totalOrderAmount)