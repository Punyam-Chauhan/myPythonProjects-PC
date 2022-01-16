import random
import os
import time
choice = ["P", "R", "S", "Q"]
i = 0
NoneA = ""


def gamewin(comp, y):
    global i
    if y in choice:

        # for E
        if y == "Q":
            print(i)
            exit()

    # for P
        if comp == "P":
            if y == "R":
                return False
            elif y == "S":
                return True

    # for R
        if comp == y:
            return NoneA
        elif comp == "R":
            if y == "S":
                return False
            elif y == "P":
                return True

    # for S
        elif comp == "S":
            if y == "P":
                return False
            elif y == "R":
                return True
    else:
        print("Please Enter a Valid Choice!")


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


clearConsole()
print("Welcome to Rock, Paper and Scissors!")
time.sleep(0.3)
ppp = input("Press: \n (P)to play \n (G) for guide \n (E) to exit \n")
ppp = ppp.upper()
if ppp == "G":
    print("Press (P) for paper, (R) for rock & (S) for scissors")
    while True:
        print("It's Computer turn")
        a = random.randint(1, 3)
        if a == 1:
            comp = "R"
        elif a == 2:
            comp = "P"
        elif a == 3:
            comp = "S"
        time.sleep(1.2)
        you = input("Your turn, enter rock(R), paper(P), scissor(S) or Quit(Q)")
        you = you.upper()

        pas = gamewin(comp, you)

        print("Computer Chose:", comp)
        print("You Chose:", you)

        if pas == NoneA:
            print("The game is tie!")
        elif pas == True:
            print("You Win!")
            i = i+1
        elif pas == False:
            print("You lose!")
if ppp == "P":

    while True:
        print("It's Computer turn")
        a = random.randint(1, 3)
        if a == 1:
            comp = "R"
        elif a == 2:
            comp = "P"
        elif a == 3:
            comp = "S"
        time.sleep(1.2)
        you = input("Your turn, enter rock(R), paper(P), scissor(S) or Quit(Q)")
        you = you.upper()

        pas = gamewin(comp, you)

        print("Computer Chose:", comp)
        print("You Chose:", you)

        if pas == NoneA:
            print("The game is tie!")
        elif pas == True:
            print("You Win!")
            i = i+1
        elif pas == False:
            print("You lose!")
elif ppp == "E":
    exit()
else:
    print("Enter a valid Choice")
