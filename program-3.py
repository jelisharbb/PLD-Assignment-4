print ("\nWelcome to Apple Store!")

def appleDtls ():
    userMny = float(input("How much money do you have? "))
    applePrc = float(input("How much is the cost of an apple each? "))
    return userMny, applePrc

user_money, apple_prc = appleDtls()

def userRcpt (money, apple):
    if money >= apple:
        receipt = money % apple
        appleQntty = money // apple
        print (f"You can buy {appleQntty} and you have a change of {receipt:,.2f} PHP.")
    elif:
        moneyShrt = apple - money
        print (f"Sorry, but you do not have enough money to buy an apple. You need {moneyShrt:,.2f} more.")
