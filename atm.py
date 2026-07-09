print("="*30)
print("      SAFE ATM SYSTEM    ")
print("="*30 +"\n")

balance=10000
print(f"Balance : {balance}")

try:
    user_amount=int(input("Enter the amount to be withdrawn:"))

    if user_amount <0:
        print("Invalid amount. You cannot withdraw a negative amount.")
    elif user_amount > balance:
        print("insufficient balance. ")
    else:
        remaining_amount=balance-user_amount
        print("Withdrawal successfully")
        print(f"Remaining amount : {remaining_amount}")

except ValueError:
    print("Invalid input. please enter a valid number.")

finally:
    print("Thank you for using ATM!")
