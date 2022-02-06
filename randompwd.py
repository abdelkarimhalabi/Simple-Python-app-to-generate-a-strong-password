import random
import string

#function to check if the number entered from user is number and not a string or character
def isInt(x):
    try:
        x = int(x)
        return True
    except:
        return False

#function to check if the number entred by user is  out of range of choices or no
def isValid(x):
    if x != 1 and x != 2 and x!= 3:
        return False
    else:
        return True

#function to generate the password
def PasswordGenerator(n):
    alphabet = string.ascii_letters
    characters = string.punctuation
    numbers = string.digits
    length = 0
    password = ""

    if n == 1:
        length = random.randint(5,8)
        while len(password) < length-1:
            x = random.randrange(1,3)
            if x == 1:
                password += alphabet[random.randint(0,51)]
            else:
                 password += numbers[random.randint(0,9)]

        password += characters[random.randint(0,31)]
        return password
    
    elif n == 2:
        length = random.randint(9,14)
        while len(password) < length-3:
             x = random.randrange(1,3)
             if x == 1:
                 password += alphabet[random.randint(0,51)]
             else:
                 password += numbers[random.randint(0,9)]
        for i in range(0,3):
            password += characters[random.randint(0,31)]
        return password

    elif n == 3:
        length = random.randint(17,24)
        while len(password) <= length:
            for i in random.choice("123"):
                if i == "1":
                    password += alphabet[random.randint(0,51)]
                if i == "2":
                    password += characters[random.randint(0,31)]
                if i == "3":
                    password += numbers[random.randint(0,9)]
        return password

#function to let the user correct his wrong entry 
def correction(x):
    x = int(x)
    while isValid(x) == False:
        x= input("Please enter a valide number: ")
        while isInt(x) == False:
            print("Please enter a number !!!!!!!!!")
            x = input("Enter the number here : ")
            if isInt(x) == True:
                break
        if isValid(int(x)) == True:
            break
    
    print(f"Your Password is: {PasswordGenerator(int(x))}")

print("What level of security you want?\nplease choose the corresponding number of the level that you want")
print("1)Low\n2)Medium\n3)High\n")

#reading an input from the user
x = input("Enter the number here : ")

if isInt(x) == True:
    if isValid(int(x)) == True:
        print(f"Your Password is: {PasswordGenerator(int(x))}")

    else:
        correction(x) 
    

else:
    while isInt(x) == False:
        print("Please enter a number !!!!!!!!!")
        x = input("Enter the number here : ")
        if isInt(x) == True:
            break
    correction(x)        

