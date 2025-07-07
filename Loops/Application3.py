import random

number = random.randint(1, 100)
count = 5

print("Number : ", number)
while count > 0:
    userNumber = int(input("Enter a number between 1 and 100: "))
    if userNumber < 0 or userNumber > 100:
        print("Please enter a number between 1 and 100")

    if userNumber == number:
        print("You have won the game!")
        break

    if userNumber < number:
        print("Please up to number value")

    if userNumber > number:
        print("Please down to number value")

    count -= 1
    if count == 0:
        print("Game Over")
        break