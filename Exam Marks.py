print("""
########################
# Exam Marks #
# IF ELIF ELSE TESTING #
# Example Program #
########################
""")
print("Enter Exam Marks :")
mark =int(input())
if (mark < 40 ):
    print("You Fail Exam")
elif(mark <=55):
    print("You Pass Exam But Marks Not Good")
elif(mark <=70):
    print("You Pass Exam But Marks is Normal")
elif(mark <=80):
    print("You Pass Exam and Marks is Good")
elif(mark <= 100):
    print("You Pass Exam and Marks is Excellent")
else:
    print("Input Error!")
