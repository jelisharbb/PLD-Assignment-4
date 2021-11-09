print ("\nWelcome to Apple Store!")

def appleDtls ():
    userMny = float(input("\nHow much money do you have? "))
    applePrc = float(input("How much is the cost of an apple each? "))
    return userMny, applePrc

user_money, apple_prc = appleDtls()

def userRcpt (money, apple):
    if money >= apple:
        receipt = money % apple
        appleQntty = money // apple
        print (f"\nYou can buy {appleQntty} apple/s and your change is {receipt:,.2f} PHP. Happy shopping! \n")
    else:
        moneyShrt = apple - money
        print (f"\nSorry, but you do not have enough money to buy an apple. You need {moneyShrt:,.2f} PHP more. \n")

userRcpt (user_money, apple_prc)
