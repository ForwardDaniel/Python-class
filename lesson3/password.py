def validate():
    while True:
        password = input("Input your Password")
        if len(password) < 8:
            print ("Password must be more than 8 Characters")
        #return:
        else:

            print("password correct")
            break