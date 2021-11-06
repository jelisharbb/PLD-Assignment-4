def getNameAgeAddress():
    user_name = input("\nEnter your name: ")
    user_age = int(input("Enter your age: "))
    user_address = input("Enter your address: ")
    return user_name, user_age, user_address

name, age, address = getNameAgeAddress()

print (f"\nHi, my name is {name}. I am {age} years old and I live in {address}. \n")