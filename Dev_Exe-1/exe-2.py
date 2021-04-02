val = int(input("Enter your value: "))
print(val)


def prime(val):
    flag = False
    if val > 1:

     for i in range(2, val):
        if (val % i) == 0:

            flag = True

            break
    if flag:
      print(val, "is not a prime number")
    else:
      print(val, "is a prime number")

prime(val)