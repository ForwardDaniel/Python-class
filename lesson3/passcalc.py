print ("Enter user name")
UserName = str(input())
password = input ("Enter Your Password")
if len(password) < 8:
    print ("Password must be more than 8 character")
else:
    print ("Password Correct")
print ("User name is", UserName)