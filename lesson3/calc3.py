while True:
    password = input("Input your Password")
    if len(password) < 8:
        print ("Password must be more than 8 Characters")
    elif len(password)> 8:
            break
            if validate():
                    def add(x,y):
                            return x + y
def subtract (x, y):
        return x - y
def multiply (x, y):
        return x * y
def divide (x, y):
        return x / y
        print ("Select Operation.")
        print ("+")
        print ("-")
        print ("*")
        print ("/")
choice = input("Enter choice + or - or * or / ")
num1 = int(input ("Enter The First Number:"))
num2 = int(input ("Enter The Second Number:"))
if choice == '+':
        print(num1, "+", num2, "=", add(num1,num2))
elif choice == '-':
        print(num1, "-", num2, "=", subtract(num1, num2))
elif choice == '*':
        print(num1, "*", num2, "=", multiply(num1, num2))
elif choice == '/':
         print(num1, "/", num2, "=", divide(num1, num2))
else:
            print("Invalid Input")