#3. in a certain shop taxes are imposed basing on the amount of cash spent using the table below
#print out the total cash spent for customers who bought goods worth the following amounts.
#i. 2500
#ii. 10000
#iii. 25000
#iv. 70000

value1=int(input("Enter Value of Goods 1:"))
if value1 >=0 and value1 <=1000:
    tax1 = (int(100))
    print(tax1)
elif value1 >=1001 and value1 <=5000:
    tax1 = (int(250))
    print(tax1)
elif value1 >=5001 and value1 <=15000:
    tax1 = (int(300))
    print(tax1)
elif value1 >=15001 and value1 <=30000:
    tax1 = (int(400))
    print(tax1)
elif value1 >30000:
    tax1 = (int(500))
    print(tax1)
else:
    print("Enter Correct value")

value2=int(input("Enter Value of Goods 2:"))
if value2 >=0 and value2 <=1000:
    tax2=(int(100))
    print(tax2)
elif value2 >=1001 and value2 <=5000:
    tax2=(int(200))
    print(tax2)
elif value2 >=5001 and value2 <=15000:
    tax2 = (int(300))
    print(tax2)

elif value2 >=15001 and value2 <=30000:
    tax2 = (int(400))
    print(tax2)

elif value2 >30000:
    tax2 = (int(500))
    print(tax2)
else:
    print("Enter Correct value")

value3=int(input("Enter Value of Goods 3:"))
if value3 >=0 and value3 <=1000:
    tax3 = (int(100))
    print(tax3)
elif value3 >=1001 and value3 <=5000:
    tax3 = (int(250))
    print(tax3)
elif value3 >=5001 and value3 <=15000:
    tax3 = (int(300))
    print(tax3)
elif value3 >=15001 and value3 <=30000:
    tax3 = (int(400))
    print(tax3)
elif value3 >30000:
    tax3 = (int(500))
    print(tax3)
else:
    print("Enter Correct value")


value4=int(input("Enter Value of Goods 3:"))
if value4 >=0 and value4 <=1000:
    tax4 = (int(100))
    print(tax4)
elif value4 >=1001 and value4 <=5000:
    tax4 = (int(250))
    print(tax4)
elif value4 >=5001 and value4 <=15000:
    tax4 = (int(300))
    print(tax4)
elif value4 >=15001 and value4 <=30000:
    tax4 = (int(400))
    print(tax4)
elif value4 >30000:
    tax4 = (int(500))
    print(tax4)
else:
    print("Enter Correct value")

print("Total Tax cash",tax1+tax2+tax3+tax4)
print("Total Value of Goods",value3+value2+value1+value4)