number = int(input("Enter a number : "))
isAsal = False
i = 2
while i < number:
    if number % i == 0:
        isAsal = False
        break
    else:
        isAsal = True

    i += 1

if isAsal or number == 2 or number == 1:
    print("Girilen sayı bir asal sayıdır")
else:
    print("Girilen sayı bir asal sayı değildir")