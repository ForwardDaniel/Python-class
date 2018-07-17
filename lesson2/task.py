print("Enter the first radius")
r1 = int(input())
print("Enter the second radius")
r2 = int(input())
area1 = 3.14*r1*r1
print (area1)
area2 = 3.14*r2*r2
print (area2)

area = (area1,area2) #tuple
print (area)
area = [area1,area2] #list
print (area)
area[0]=1522 #update or replace
print (area)

details = {r1:area1,r2:area2}
print (details)

print(details.keys())
print(details.values())