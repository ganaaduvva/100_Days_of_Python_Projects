
print("---------------------------------------------------")
print("       ***  Welcome to Tip Calculator!  ***        ")
print("---------------------------------------------------\n")

totalBill = float(input("What is the total bill?\n$"))
tipToAdd = int(input("what percentage tip would you like to give? 10, 12 or 15?\n"))

tipPercentage = 0.01 * tipToAdd + 1
totalBillWithTip = totalBill * tipPercentage

splitBill = int(input("How many people to split the bill?\n"))
eachPersonToPay = totalBillWithTip / splitBill

print("")
print(f"--> Each person should pay: ${round(eachPersonToPay, 2)}")
