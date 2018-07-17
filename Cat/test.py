value1=int(input("Enter Value of Goods 1:"))
if value1 >=0 and value1 <=1000:
    print("100")
elif value1 >=1001 and value1 <=5000:
    print("250")
elif value1 >=5001 and value1 <=15000:
    print("300")
elif value1 >=15001 and value1 <=30000:
    print("400")
elif value1 >30000:
    print("500")
else:
    print("Enter Correct value")

value2=int(input("Enter Value of Goods 2:"))
if value2 >=0 and value2 <=1000:
    tax=(int(100))
    print(tax)
elif value2 >=1001 and value2 <=5000:
    print(int(200))
elif value2 >=5001 and value2 <=15000:
    print(int(300))
elif value2 >=15001 and value2 <=30000:
    print(int(400))
elif value2 >30000:
    print(int(500))
else:
    print("Enter Correct value")

value3=int(input("Enter Value of Goods 3:"))
if value3 >=0 and value3 <=1000:
    print("100")
elif value3 >=1001 and value3 <=5000:
    print("250")
elif value3 >=5001 and value3 <=15000:
    print("300")
elif value3 >=15001 and value3 <=30000:
    print("400")
elif value3 >30000:
    print("500")
else:
    print("Enter Correct value")

print("Total cash",value1+value2+value3)