# name = input("Enter your name : ")
# age = input("Enter your age : ")
# educationStatus = input("Enter your education status(lise, üniversite....) : ")
#
# if int(age) >= 18 and (educationStatus == 'lise' or educationStatus == 'üniversite'):
#     print(f"{name}, you can get driver license")
# else:
#     print(f"{name}, you can not get driver license")


print("*****************************************************")


writtenGrade1 = input("Enter your written note 1 : ")
writtenGrade2 = input("Enter your written note 2 : ")
verbalGrade = input("Enter your verbal note : ")

totalNote = float(float(writtenGrade1) + float(writtenGrade2) + float(verbalGrade))
averageNote = totalNote / 3

if 0 <= averageNote <= 24:
    print(f"Your average note is {averageNote:.2f}. Note Value : 0")
elif 25 <= averageNote <= 44:
    print(f"Your average note is {averageNote:.2f}. Note Value : 1")
elif 45 <= averageNote <= 54:
    print(f"Your average note is {averageNote:.2f}. Note Value : 2")
elif 55 <= averageNote <= 69:
    print(f"Your average note is {averageNote:.2f}. Note Value : 3")
elif 70 <= averageNote <= 84:
    print(f"Your average note is {averageNote:.2f}. Note Value : 4")
elif averageNote >= 85:
    print(f"Your average note is {averageNote:.2f}. Note Value : 5")
else:
    print("Your not is undefined note value")