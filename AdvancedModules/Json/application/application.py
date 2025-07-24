import json
import os.path


class User:
    def __init__(self, username:str, password:str, email:str):
        self.username = username
        self.password = password
        self.email = email


class UserRepository:
    def __init__(self):
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        self.loadUser()

    def loadUser(self):
        if os.path.exists("users.json"):
            with open('users.json', 'r', encoding="utf-8") as file:
                users = json.load(file)
                for user in users:
                    userData = json.loads(user)
                    newUser = User(username=userData['username'], password=userData['password'], email=userData['email'])
                    self.users.append(newUser)

    def register(self, user: User):
        self.users.append(user)
        self.saveToFile()
        print("User generated ✅")
        pass

    def login(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                self.isLoggedIn = True
                self.currentUser = user

                print("Logged to system 🎯")
                break

    def logout(self):
        self.currentUser = {}
        self.isLoggedIn = False

        print("Exited from system 👋🏼")

    def identity(self):
        if self.isLoggedIn:
            if self.currentUser:
                currentUser = self.currentUser
                print(f'🧑🏽‍💻Username : {currentUser.username} \n📧E-Mail : {currentUser.email}')
        else:
            print("There is no logged user in the system. Please sign in 🚨")

    def saveToFile(self):
        usersList = []
        for userObj in self.users:
            usersList.append(json.dumps(userObj.__dict__))

        with open('users.json', 'w') as file:
            json.dump(usersList, file)



repository = UserRepository()
print(repository.users)
while True:
    print('Menü'.center(50,'*'))
    select = input("1 - Register \n2 - Login \n3 - Logout \n4 - Identity \n5 - Exit \nYour Select : ")
    if select == '5':
        print("Good Bye 👋🏼")
        break
    else:
        if select == '1':
            username = input("Username : ")
            password = input("Password : ")
            email = input("E-Mail : ")

            user = User(username=username, password=password, email=email)
            repository.register(user)
        elif select == '2':
            username = input("Username : ")
            password = input("Password : ")

            repository.login(username=username, password=password)
        elif select == '3':
            repository.logout()
        elif select == '4':
            repository.identity()
        else:
            print("Error : Invalid select value. System stopped")
            break
