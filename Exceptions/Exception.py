try:
    x = int(input("Enter a number: "))
    y = int(input("Enter a number: "))
    print("Result : ", x/y)
except Exception as error:
    print("Invalid number. Error : ", error)
finally:
    print("Try-except sonlandı")

