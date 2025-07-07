from OOP.Inheritance.Person import Person


class Student(Person):
    def __init__(self):
        super().__init__()
        # Person.__init__(self)
        print("Student Generated")