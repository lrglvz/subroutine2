# Create a program which you will enter the amount of money you have,
# it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format: You can buy ___ apples and your change is ___ pesos.

# Step 1: Create functions with multiple returned values.
def displayIntro():
    print(f"A conversation between a vendor and a buyer.")
    print(f"Vendor: How much money do you have? ")

def getPriceMoney():
    moneyAmount = int(input("Buyer: "))
    print(f"Buyer: How much is an apple?")
    applePrice = int(input("Vendor: "))
    return moneyAmount, applePrice

def displayOutput(maximumApple, change): # no multiple returned values needed.
    print(f"Vendor: You can buy {maximumApple} apple/s and your change is {change} peso/s.")

# Step 2: Display Introduction (additional information)
displayIntro()

# Step 3: Ask for the price of an apple and the amount of money.
money, price = getPriceMoney()

# Step 4: Finally, display the output.
displayOutput(money//price, money%price)