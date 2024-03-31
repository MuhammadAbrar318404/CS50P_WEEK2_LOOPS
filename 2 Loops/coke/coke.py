# Defining the main function
def main():
# calling the due amount function
    check_balance()
def check_balance():
#As by default total due is 50
    due=50
    accept_coin=[5,10,25]
# Loop to ask for coin unless due become 0 or negative
    while due>0:
        print("Amount Due:", due)
        coin=int(input("Insert Coin:"))
# Only accepts the 5,10, and 25 coins
        if coin in accept_coin:
# updating the due after getting coin
            due=due-coin
# Calculating the change
            if due<0:
                due1=-due
            else:
                due1=due
        else:
            pass
    print("Change Owed:",due1)
#Calling the main function
main()
