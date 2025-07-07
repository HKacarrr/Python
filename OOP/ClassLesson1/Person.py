from datetime import datetime

class Person:
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def calculateAge(self):
        currentTime = datetime.now()
        return currentTime.year - self.year


p1 = Person("Hasan Kacar", 1999)
print(f"Person name : {p1.name} && year : {p1.year} && age : {p1.calculateAge()}")

