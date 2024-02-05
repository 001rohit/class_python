class student():
      name=""
      roll_no=0
      def set_data(self):
            self.name = input("Enter student Name: ")
            self.roll_no=int(input("Enter roll number: "))
      def print_detail(self):
            print("Student name is: ",self.name)
            print("Your roll number is: ",self.roll_no)


person1 = student()
person1.set_data()
person1.print_detail()