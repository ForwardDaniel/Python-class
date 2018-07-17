#4. Write a python program to implement a login system and hence implement a python calculator
#define the login system on an external module on a function
#NB all inputs from the user
def validate():
    while True:
        password = input("Input your Password")
        if len(password) < 8:
            print ("Password must be more than 8 Characters")
        #return:
        else:

            print("password correct")
            break