#2. In question 1 above write a python program to grade the students
AverageScore = int(input("What was your average Score?"))

if AverageScore >=80 and AverageScore <=100:
    print("Your Score is: A")
elif AverageScore >=70 and AverageScore <=79:
    print("Your Score is: B")
elif AverageScore >= 60 and AverageScore <= 69:
    print("Your Score is: C")
elif AverageScore >=50 and AverageScore <=59:
    print("Your Score is: D")
elif AverageScore >=40 and AverageScore <=49:
    print("Your Score is: E")
elif AverageScore >=0 and AverageScore <=39:
    print("Your Score is: Fail")
else:
    print("Unknown grade")
