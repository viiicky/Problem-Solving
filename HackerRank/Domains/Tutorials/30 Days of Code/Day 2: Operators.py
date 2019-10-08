mealCost = float(input())
tipPercentage = int(input())
taxPercentage = int(input())

print("The total meal cost is " + str(round(mealCost + 0.01*tipPercentage*mealCost + 0.01*taxPercentage*mealCost)) + " dollars.")
