purchase = int(input("Enter your total purchase: "))
print(purchase)

def calculatePoints(total_purchases):
    if 0 <= total_purchases < 100:
        print("Your point is 10")
    elif 100<= total_purchases < 500:
        print("Your point is 20")
    elif 500 < total_purchases:
        print("Your point is 50")

calculatePoints(purchase)