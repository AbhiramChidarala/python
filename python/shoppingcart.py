#shopping cart program 
foods =[]
prices = []
total =0

while True:
    food = input("Enter a food to buy (q to quit ) :" )
    if food.lower() =="q":
        break
    else : 
        price = float(input("Enter the price of a {food}: ₹ "))
        foods.append(food)
        prices.append(price)

print("-------YOUR CART------- ")

for food, price in zip(foods, prices):
    print(f"{food}: ₹ {price}")

total = sum(prices)
print(f"total amount to pay is : ₹ {total}")
