class Student:
    studCount = 0

    def __init__(self, name, StdClass, Admission):
        self.name = name
        self.StdClass = StdClass
        self.Admission = Admission

        Student.studCount+=1

    def displayCount(self):
        print("Total Students = %d" % Student.studCount)

student1 = Student((),(),())
print ("Enter Student 1 Name")
student1.name = (input())

print ("Enter Student 1 Class")
student1.StdClass = (input())

print ("Enter Student 1 Admission")
student1.Admission = (input())



student2 = Student((),(),())
student2.name = "Nick"
student2.StdClass = "Form 3"
student2.Admission = "111"

student3 = Student((),(),())
student3.name = "James"
student3.StdClass = "Form 1"
student3.Admission = "333"

student4 = Student((),(),())
student4.name = "Allan"
student4.StdClass = "Form 4"
student4.Admission = "444"

student5 = Student((),(),())
student5.name = "Kass"
student5.StdClass = "Form 1"
student5.Admission = "555"

print (student1.name, student1.StdClass, student1.Admission)
print (student2.name, student2.StdClass, student2.Admission)
print (student3.name, student3.StdClass, student3.Admission)
print (student4.name, student4.StdClass, student4.Admission)
print (student5.name, student5.StdClass, student5.Admission)

Student.displayCount(student1)