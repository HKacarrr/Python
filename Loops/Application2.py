# numbers = [1, 3, 5, 7, 9, 12, 19, 21]
#
# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i += 1


firstNumber = int(input("Please enter a first number : "))
lastNumber = int(input("Please enter a last number : "))

while firstNumber <= lastNumber:
    if firstNumber % 2 != 0:
        print(firstNumber)
    firstNumber +=  1
