#lower= int(input("Enter lower range"))
#upper= int(input("Enter upper range"))
for num in range(2,100):
    if num > 1:
        for item in range(2,num):
            if(num%item)==0:
                break
        else:
            print (num)