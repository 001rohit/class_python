class student():
    name = ""
    roll_number = 0
    mobile_no = 0
    address = ""
    def set_inputData(self):
          self.name=input("Enter your name: ")
          self.roll_number=int(input("Enter your roll number: "))
          self.mobile=int(input("Enter your mobile number: "))
          self.address=input("Enter your address: ")

    def print_data(self):
         print()
         print("Your name is: ",self.name)
         print("Your roll number is: ",self.roll_number)
         print("Your mobile number is: ",self.mobile)
         print("Your address is: ",self.address)

Sam = student()
John = student()
Sam.set_inputData()
Sam.print_data()

John.set_inputData()
John.print_data()

