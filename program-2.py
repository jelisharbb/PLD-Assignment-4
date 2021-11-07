print ("\nWelcome to Fruit Market! \nHere's our pricelist: \n> Apples = 20 PHP \n> Orange = 25 PHP \n")
 
def getQuantity():
    appleQuan = int(input("How many apple/s do you want to purchase? "))
    orangeQuan = int(input("How many orange/s do you want to purchase? "))
    grandTtl = fruitPrc(apple=appleQuan, orange=orangeQuan)
    print (f"\nThe total amount is {grandTtl:,.2f} PHP. \n")

def fruitPrc(apple, orange):
    applePrc = 20 * apple
    orangePrc = 25 * orange
    fruitTtl = applePrc + orangePrc
    return fruitTtl;

getQuantity()