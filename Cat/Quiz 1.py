#*1. write a python program to calculate the average scores of 5 classes with 10 students each and display
#the output as a
#i. tuple
#ii. list
#iii. dictionary

print ("Enter The Class")
classes1 = input()
print("Enter the scores")
scores1 = [(int(input())),+int (input()), +int(input()),+int(input()), +int(input()),+int(input()),+int(input()),+(int(input())),+int (input()), +int(input())]
total= sum(scores1)
print(total)
average1=total/10
print(average1)
#average=scores1/10

#second class
print ("Enter The Second Class")
classes2 = input()
print("Enter the scores")
scores2 = [(int(input())),+int (input()), +int(input()),+int(input()), +int(input()),+int(input()),+int(input()),+(int(input())),+int (input()), +int(input())]
total2= sum(scores2)
print(total2)
average2=total2/10
print(average2)

#third class
print ("Enter The third Class")
classes3 = input()
print("Enter the scores")
scores3 = [(int(input())),+int (input()), +int(input()),+int(input()), +int(input()),+int(input()),+int(input()),+(int(input())),+int (input()), +int(input())]
total3= sum(scores3)
print(total3)
average3=total3/10
print(average3)


#forth class
print ("Enter The forth Class")
classes4 = input()
print("Enter the scores")
scores4 = [(int(input())),+int (input()), +int(input()),+int(input()), +int(input()),+int(input()),+int(input()),+(int(input())),+int (input()), +int(input())]
total4= sum(scores4)
print(total4)
average4=total4/10
print(average4)


#fifth class
print ("Enter The Fifth Class")
classes5 = input()
print("Enter the scores")
scores5 = [(int(input())),+int (input()), +int(input()),+int(input()), +int(input()),+int(input()),+int(input()),+(int(input())),+int (input()), +int(input())]
total5= sum(scores5)
print(total5)
average5=total5/10
print(average5)

print("Average scores in tuple",average1,average2,average3,average4,average5)

list=[average1,average2,average3,average4,average5]
print("Average scores in List",list)


scoreDictionary = {classes1:average1,classes2:average2,classes3:average3,classes4:average4,classes5:average5}
print("This is the Dictionary",scoreDictionary)
print(scoreDictionary.keys())
print(scoreDictionary.values())