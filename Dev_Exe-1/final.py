my_list=[]
temp_list=[]
n=int(input('Enter the size of the student list '))


for i in range(n):
    for j in range(0,1):
        temp_list.append(input("Enter person's ID "))
        temp_list.append(input("Enter person's Last Name "))
        temp_list.append(input("Enter person's First Name "))
        #marks = int(input("Enter person's Marks "))
        while(True):
            in_num = int(input("Enter person's Marks : "))
            if in_num not in range(1,101):
               print("enter a valid number between 1 and 100")
            else:
               temp_list.append(in_num)
               break
    my_list.append(temp_list)
    temp_list=[]
print("Total Student list is: ")
print(my_list)
print("85+ Scoring Students are: ")
for i in range(len(my_list)):
    if my_list[i][3] > 85:
        print(my_list[i])
        i = i+1
    else:
        i = i+1


