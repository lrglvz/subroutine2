# Create a program that will ask how many apples and oranges you want to buy. 
# Display the total amount you need to pay if apple is P20 and orange is P25.
# Display the output in the following format: The total amount is ________.

# Step 1: Create functions with multiple returned values.
def displayIntro(): # additional information no multiple returned values needed.
    print(f"You're in a market because you need to buy fruits for your sick partner, an apple is 20 pesos and an orange is 25.")

def getTotalAmount():
    apples_ = int(input("How many apples you want to buy? "))
    applePrice_ = 20
    oranges_ = int(input("How many oranges you want to buy? "))
    orangePrice_ = 25
    return apples_, applePrice_, oranges_, orangePrice_

def displaySolution(apple, appleprice, orange, orangeprice): # additional information no multiple returned values needed.
    print(f"(Solution: ({apple} x {appleprice}) + ({orange} x {orangeprice}) = ?)")


def displayTotalAmount(amountF): # no multiple returned values needd.
    print(f"The total amount is {amountF}.")

# Step 2: Introduction (additional information)
displayIntro()

# Step 3: Ask how many apples and oranges the user wants to buy.
apples, appleP, oranges, orangeP = getTotalAmount()

# Step 4: Display the solution (additional information)
displaySolution(apples, appleP, oranges, orangeP)

# Step 5: Display the output with the format given.
displayTotalAmount(apples*appleP + oranges*orangeP)