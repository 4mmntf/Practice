print("hellow")
apple = input("How many apples do you want")
apple = int(apple)
apple_price = 100
orange = input("How many oranges do you want")
orange = int(orange)
orange_price = 50
watermelon = input("How many watermelon do you want")
watermelon = int(watermelon)
watermelon_price = 500
sum = apple*apple_price + orange*orange_price + watermelon*watermelon_price
print("Please pay off " + str(sum) + "yen")