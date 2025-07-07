import math

numbers = [1, 3, 5, 7, 9, 12, 19, 21]
resultArr = []
totalNumberVal = 0

# for number in numbers:
#     if number % 3 == 0:
#         resultArr.append(number)


# for number in numbers:
#     totalNumberVal += number



for number in numbers:
    result = math.pow(number, 2)
    resultArr.append(int(result))

print(resultArr)