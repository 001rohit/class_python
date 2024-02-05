class student() :
    name = ""
    age = 0
    marks = []
  
    def set_data(self):
        self.name=input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        lst = []
        for i in range(5):
            intVal = int(input("Enter your marks: "))
            lst.append(intVal)

        self.marks = lst

    def print_data(self):
        print()
        print("Your name is: ",self.name)
        print("Your age is: ",self.age)
        print("Your marks is: ",self.marks)

user1 = student()
user2 = student()
user1.set_data()
user2.set_data()
user2.print_data()