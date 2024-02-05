class student() :
    name = ""
    age = 0
    marks = []

    def print_data(self):
        print()
        print("Your name is: ",self.name)
        print("Your age is: ",self.age)
        print("Your marks is: ",self.marks)

object1 = student()
object1.name=input("Enter your name:  ")
object1.age=int(input("Enter your age:  "))
marks=[]

for i in range(5):
    intVal = int(input("Enter your marks: "))
    marks.append(intVal)
object1.marks = marks

object1.print_data()


object2 = student()
object2.name=input("Enter your name:  ")
object2.age=int(input("Enter your age:  "))
marks=[]

for i in range(5):
    intVal = int(input("Enter your marks: "))
    marks.append(intVal)
object2.marks = marks

object2.print_data()

object3 = student()
object3.name=input("Enter your name:  ")
object3.age=int(input("Enter your age:  "))
marks=[]

for i in range(5):
    intVal = int(input("Enter your marks: "))
    marks.append(intVal)
object3.marks = marks

object3.print_data()


