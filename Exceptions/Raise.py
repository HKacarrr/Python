class PasswordChecker:
    def __init__(self, password):
        self.password = password

    def check(self):
        import re
        if len(self.password) < 8:
            raise Exception("Password must be at least 8 characters long")
        elif not re.search("[A-Z]", self.password):
            raise Exception("Password must contain at least one uppercase letter")
        elif not re.search("[a-z]", self.password):
            raise Exception("Password must contain at least one lowercase letter")
        elif not re.search("[0-9]", self.password):
            raise Exception("Password must contain at least one number")
        elif not re.search("[_@$]", self.password):
            raise Exception("Password must contain at least one punctuation")
        elif re.search(r"\s", self.password):
            raise Exception("Password must not contain at least one space")



try:
    password = input("Enter password : ")
    passwordChecker = PasswordChecker(password)
    passwordChecker.check()
except Exception as e:
    print(e)
else:
    print("Password is ok. Password : ", password)
finally:
    print("Exception control finished")