balance = 50000

withdraw = int(input("How much do you want to withdraw? "))

if withdraw <= balance:
    print("Transaction Successful")
    print("Remaining Balance:", balance - withdraw)
else:
    print("Insufficient Funds")