import math

# print(math.sqrt(25))
# print(math.pow(16,2))
# print(math.factorial(5))

# num1 =4
# num2 = 16
# lcm = num1*num2/math.gcd(num1,num2)

# print(lcm)

# print(math.floor(23.5))
# print(math.pi)

class Calculator:
    lst1 = []
    def __init__(self,num1,num2):
         self.num1=num1
         self.num2=num2
   
    def Sum(self):
        print(f"The sum of to number is: {self.num1 + self.num2}")

    def Sub(self):
        print(f"The substraction of to number is: {self.num1-self.num2}")

    def Multi(self):
        print(f"The Multiplication of to number is: {self.num1*self.num2}") 

    def Devi(self):
        print(f"The divition of to number is: {self.num1/self.num2}") 
   
    def Square(self):
         print(f"The Square of first number is : {math.pow(self.num1,2)}")
         print(f"The Square of second number is : {math.pow(self.num2,2)}")

    def Qube(self):
         print(f"The Square of first number is : {math.pow(self.num1,3)}")
         print(f"The Square of second number is : {math.pow(self.num2,3)}")

    def Factor(self):
         print(f" Factorial of first number is : {math.factorial(self.num1)}")
         print(f" Factorial of second number is : {math.factorial(self.num2)}")
 
    def LCM(self):
         lcm = self.num1*self.num2/math.gcd(self.num1,self.num2)
         print(f"Lcm  : {lcm}")

    def Sqrt(self):
         print(f" Square root of first number is : {math.sqrt(self.num1)}")
         print(f" Square root of second number is : {math.sqrt(self.num2)}")

    def Table(self):
          print("\n Table of : ",self.num1)
          a = 1
          while(a<=10):
                print(self.num1,"*",a,"=",a*self.num1)
                a+=1
          print()
          print("\n Table of : ",self.num2)
          a=1
          while(a<=10):
                print(self.num2,"*",a,"=",a*self.num2)
                a+=1


    def Check_Prime(self):
            print()
            count = 0
            for i in range(1,self.num1+1):
                if(num1%i==0):
                        count+=1    
            if(count==2):
                print("Give number is prime ")
            else:
                print("Give number is not prime")
            count1 = 0
            for i in range(1,self.num2+1):
                if(num2%i==0):
                        count1+=1    
            if(count1==2):
                print("Give number is prime ")
            else:
                print("Give number is not prime") 


num = 0
while num!=12:
    print("\n\n1. addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Divition")
    print("5 Square")
    print("6 Cube")
    print("7 Factorial")
    print("8 LCM")
    print("9. Square Root")
    print("10. Table")
    print("11. check Prime number")
    print("12. Exit")

    num = int(input("Enter your choice: "))

    if(num==12):
        break
    
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    lst = Calculator(num1,num2)
    
    if(num==1):
            lst.Sum()

    elif(num==2):
            lst.Sub()
    
    elif(num==3):
            lst.Multi()

    elif(num==4):
            lst.Devi()

    elif(num==5):
            lst.Square()

    elif(num==6):
            lst.Factor()     

    elif(num==7):
            lst.LCM()  

    elif(num==8):
            lst.Sqrt()   
  
    elif(num==9):
            lst.Qube()   

    elif(num==10):
            lst.Table()

    elif(num==11):
            lst.Check_Prime()   