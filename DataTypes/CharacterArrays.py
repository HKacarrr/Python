from dataclasses import replace

course = "Python Kursu : Baştan Sona Python Programlama Rehberiniz (40 Saat)"
website = "http://www.sadikturan.com"

courseLength = len(course)
print("Text Length : ", courseLength)


wwwCharacters = website[7:10]
print("WWW Characters : ", wwwCharacters)


comCharacters = website[len(website) - 3:len(website)]
print("COM Characters : ", comCharacters)


reverseCourse = course[::-1]
print("Reverse Course Characters : ", reverseCourse)


helloWorld = "Hello world"
print("Hello World Revision : ", helloWorld.replace("w", "W"))


name = "Hasan Kacar"
age = 26
job = "Computer engineer"
print(f"My name is {name}. I am {age} years old. I am a {job}")