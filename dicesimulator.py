import random

x = "Y"

while x == "Y":
    ran = random.randint(1,6)
    if ran == 1:
        print(" ----------- ")
        print("|           |")
        print("|     O     |")
        print("|           |")
        print(" ----------- ")

    elif ran == 2:
        print(" ----------- ")
        print("|           |")
        print("|    O O    |")
        print("|           |")
        print(" ----------- ")

    elif ran == 3:
        print(" ----------- ")
        print("|     O     |")
        print("|     O     |")
        print("|     O     |")
        print(" ----------- ")

    elif ran == 4:
        print(" ----------- ")
        print("|   O   O   |")
        print("|           |")
        print("|   O   O   |")
        print(" ----------- ")

    elif ran == 5:
        print(" ----------- ")
        print("|   O   O   |")
        print("|     O     |")
        print("|   O   O   |")
        print(" ----------- ")

    elif ran == 6:
        print(" ----------- ")
        print("|   O   O   |")
        print("|   O   O   |")
        print("|   O   O   |")
        print(" ----------- ")

    x = input("Enter Y to continue else press N to terminate: ")
