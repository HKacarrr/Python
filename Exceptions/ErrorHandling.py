# listContent = ["1", "2", "5a", "10b", "abc", "10", "50"]
# numberValues = []
#
# try:
#     for value in listContent:
#         try:
#             numberVal = int(value)
#             numberValues.append(numberVal)
#         except ValueError:
#             continue
# except Exception as e:
#     print("An error occurred. Error : ", e)
# else:
#     print("There is not any errors on the process")
# finally:
#     print("Number Values : ", numberValues)


loopStatus = True
while loopStatus:
    try:
        value = input("Enter a number value : ")
        if value == 'q':
            loopStatus = False
        try:
            numberValue = int(value)
        except ValueError:
            print("Please enter a number")
    except Exception as error:
        print(error)
    finally:
        continue
