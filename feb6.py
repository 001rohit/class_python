#  single inheritence
class student:
    a=10
    b=20

class child(student):
     def Print(self):
          print(f"{self.a} and {self.b}")

object1 = child()
# object1.Print()

# multilevel inheritence
class parent:
     a=11

class midil(parent):
     b = 12

class last(midil):
     c=13
     def Print(self):
          print(f"{self.a},{self.b},{self.c}")

object2 = last()
# object2.Print()

# multiple inheritence
class parent:
     a=15

class midil:
     b = 12

class last(midil,parent):
     c=13
     def Print(self):
          print(f"{self.a},{self.b},{self.c}")

object3 = last()
# object3.Print()

# heirarchical inheritance
class main:
     name="Rohit"

class name1(main):
      def Print_data(self):
           print(f"1) {self.name}")

class name2(main):
      def Print_data(self):
           print(f"2) {self.name}")

class name3(main):
      def Print_data(self):
           print(f"3) {self.name}")

object1 = name1()
object2 = name2()
object3 = name3()

object1.Print_data()
object2.Print_data()
object3.Print_data()