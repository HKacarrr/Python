# number = int(input("Enter a number: "))
# if 0 < number < 100:
#     print("The number is between 0 and 100.")
# else:
#     print("The number is not between 0 and 100.")


# number = int(input("Enter a number: "))
# if number > 0 and number % 2 == 0:
#     print("The number is positive and even.")
# else:
#     print("The number is not positive or even.")



# email = "hasan.kacar@kodpit.com"
# password = "Hasan123"
#
# emailInput = input("Enter your email: ")
# passwordInput = input("Enter your password: ")
#
# if emailInput == email and passwordInput == password:
#     print("Login successful!")
# else:
#     print("Login failed! Please check your email and password.")



exam1 = int(input("Enter the score for Exam 1: "))
exam2 = int(input("Enter the score for Exam 2: "))
final = int(input("Enter the score for the Final Exam: "))

averageExamValue = (exam1 + exam2) / 2
averageNote = (averageExamValue * 0.4) + (final * 0.6)

if (averageNote >= 50 and final >= 50) or final >= 70:
    print("You passed the course.")
elif averageNote < 50 or final < 50:
    print("You failed the course.")
else:
    print("You need to retake the final exam.")

