number = input("Student Number : ")
name = input("Student Name : ")
surname = input("Student Surname : ")
phone = input("Student Phone Number : ")

students = {number: {
    'name': name,
    'surname': surname,
    'phone': phone
}}

print('Students : ', students)