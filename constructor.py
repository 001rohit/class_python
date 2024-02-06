class Student:
    roll=0
    name=""
    address = ""
    age=0

    def __init__(self,name,age,roll,address):
            self.name=name
            self.age = age
            self.roll=roll
            self.address=address

    def Print_data(self):
          print(f"Name: {self.name}")
          print(f"Age: {self.age}")
          print(f"Roll No: {self.roll}")
          print(f"Address: {self.address}")
print()
Rohit = Student("Rohit",26,32,"Bhopal")
Rohit.Print_data()
print()
Yogesh = Student("Yogesh",27,33,"Bhopal")
Yogesh.Print_data()
print()
Mukul = Student("Mukul",25,34,"Bhopal")
Mukul.Print_data()
print()
