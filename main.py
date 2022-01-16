import random
import os
def rando():
    idf = False
    i = 0
    usr = None
    ran = random.randint(strt,stp)
    while (idf == False) and (i<=7):
        i=i+1
        usr = input(f"Enter Your No. {i} Guess \n")
        if len(str(usr))!=0:
            aaa= (not (int(usr) > stp or int(usr) < strt))
            if  aaa == True:
                if ran == int(usr):
                    idf = True
                    break
                else:
                    if int(usr) >= ran:
                        print("You guessed it too high!")
                    elif int(usr) <= ran:
                        print("You Guessed it too low!")
            # elif len(str(usr))==0:
            #     print("")
            else:
                print("Number is out of range!")
        else:
            print("")
    if idf==True:
        print(f"Your Guess was correct in your {i} attempt!")
    elif idf==False:
        print(f"You Lose The Game, Number was {ran}")

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

clearConsole()
print("Welcome to Number Guesser!")
strt = int(input("Enter Start Number: \n"))
stp = int(input("Enter Stop Number \n"))
rando()