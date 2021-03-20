import sys
sys.setrecursionlimit(1000000)




def check(a):
    if a%2 == 0:
        return True
    else:
        return False


def collatz(b):
    list1=[]
    copy = b

    while b!=1:
        if check(b):
            b = b // 2
            list1.append(b)
            if b==1:
                list1.insert(0,copy)
                for i, a in enumerate(list1):
                    print(a,end =" ")
                    if i % 5 == 4:
                        print ("\n")                
                print ("\n")
                length =  len(list1)
                summation = sum(list1)
                avg = summation / length
                print("The average value is: ",avg)
        else:
            b = 3 * b + 1
            list1.append(b)
            if b==1:
                list1.insert(0,copy)
                for i, a in enumerate(list1):
                    print(a,end =" ")
                    
                    if i % 5 == 4:
                        print ("\n")
                print ("\n")
                length =  len(list1)
                summation = sum(list1)
                avg = summation / length
                print("The average value is: ",avg)         
    
    collatz(b)
    
    
    
   

a = int(input("Enter a positive number, or zero to quit\n"))

if a == 0:
    print("Have a Nice Day")
else:
    
    collatz(a)
    
    
      
