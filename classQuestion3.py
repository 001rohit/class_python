class Myclass():
    averange=0
    def input_user(self):
        sum = 0
        lst = []
        for i in range(3):
            intVal = int(input("Enter your number: "))
            lst.append(intVal)
        for i in range(len(lst)):
            sum+=lst[i]
        self.averange = sum/3
        
    def calc_Aver(self):
        print("The Average of Three numbers: ",self.averange)

user1 = Myclass()
user1.input_user()
user1.calc_Aver()

# sum = 0
# lst = []
# for i in range(3):
#     intVal = int(input("Enter your number: "))
#     lst.append(intVal)
# for i in range(len(lst)):
#     sum+=lst[i]
# print(sum)