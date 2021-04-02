import random


val = int(input("Enter your value: "))
print(val)
randomlist = random.sample(range(0, 100), val)
print(randomlist)


def check(randomlist):
    oddlist = []
    evenlist = []
    for i in range(len(randomlist)):
        if (randomlist[i] % 2) == 0:
            evenlist.append(randomlist[i])
            #print(evenlist)
        else:
          oddlist.append(randomlist[i])

    print("Odd Numbers are : ",oddlist)
    print("Even Numbers are : ",evenlist)


check(randomlist)