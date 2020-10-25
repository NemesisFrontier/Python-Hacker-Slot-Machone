import random
import pickle
import time
import tkinter as tk


def Stop():
    exit()

coins = int(0)

CoinsAmount = int(input("How many coins do you want to buy: "))
coins += (CoinsAmount)


while coins <= int(99):
    CoinsAmount = int(input("Deposit more: "))
    coins += (CoinsAmount)
GamesPlayed = 0



choices1 = ["Cherry", "Cherry", "Cherry", "Lemon", "Lemon", "Lemon", "Bar", "Bar", "Bar", "7"]
choices2 = ["Cherry", "Cherry", "Cherry", "Lemon", "Lemon", "Lemon", "Bar", "Bar", "Bar", "7"]
choices3 = ["Cherry", "Cherry", "Cherry", "Lemon", "Lemon", "Lemon", "Bar", "Bar", "Bar", "7"]


coins -= 101
coins += 1
while True:

    result1 = random.choice(choices1)


    print(result1)
    result2 = random.choice(choices2)
    time.sleep(1.0)
    print(result2)

    result3 = random.choice(choices3)
    time.sleep(1.0)
    print(result3)


    finalresult = result1, result2, result3



    if finalresult == ("Cherry", "Cherry", "Cherry"):
        FinalTextPleaseWork = ["FruitRush (+100coins)"]
        print(FinalTextPleaseWork)
        coins += int(100)

    if finalresult == ('Lemon', 'Lemon', 'Lemon'):
        FinalTextPleaseWork = ["Sour (+150coins)"]
        print (FinalTextPleaseWork)
        coins += int(150)
    if finalresult == ("Bar", "Bar", "Bar"):
        FinalTextPleaseWork = ["GoldRush (+500coins)"]
        print (FinalTextPleaseWork)
        coins += int(500)

    if finalresult == ("Bar", "Lemon", "Cherry"):
        FinalTextPleaseWork = ["Threeway (+33 coins)"]
        print (FinalTextPleaseWork)
        coins += int(33)

    if finalresult == ("Lemon", "Bar", "Cherry"):
        FinalTextPleaseWork = ["Threeway (+33 coins)"]
        print (FinalTextPleaseWork)
        coins += int(33)

    if finalresult == ("Cherry", "Lemon", "Bar"):
        FinalTextPleaseWork = ["Threeway (+33 coins)"]
        print (FinalTextPleaseWork)
        coins += int(33)

    if finalresult == ("Cherry", "Bar", "Lemon"):
        FinalTextPleaseWork = ["Threeway (+33 coins)"]
        print (FinalTextPleaseWork)
        coins += int(33)

    if finalresult == ("Lemon", "Cherry", "Bar"):
        FinalTextPleaseWork = ["Threeway (+33 coins)"]
        print (FinalTextPleaseWork)
        coins += int(33)

    if finalresult == ("7", "7", "7"):
        FinalTextPleaseWork = ["Jackpot (+1000 coins)"]
        print (FinalTextPleaseWork)
        coins += int(1000)




    print(coins, "coins")



    input1 = input("Do you want to continue: ")

    if input1 == "":
        print("")
        GamesPlayed += 1
    else:
        Stop()


    if GamesPlayed <= 30:
        choices1 = ["Cherry", "Cherry", "Cherry", "Lemon", "Bar", "7"]
        choices2 = ["Cherry", "Cherry", "Cherry", "Lemon", "Bar", "Bar", "Bar", "7"]
        choices3 = ["Cherry", "Lemon", "Bar", "Bar", "Bar", "7"]

    if GamesPlayed <= 50:
        choices1 = ["Cherry", "Cherry", "Cherry", "Lemon", "Bar", "7"]
        choices2 = ["Cherry", "Cherry", "Cherry", "Lemon", "Bar", "Bar", "7"]
        choices3 = ["Cherry", "Lemon", "Bar", "Bar", "Bar"]


    if coins <= 100:
        while coins <= int(99):
            CoinsAmount2 = (input("Deposit more: "))
            if CoinsAmount2 == (""):
                CoinsAmount2 = (input("Deposit more: "))
        if coins >= 99:
            CoinsAmount2 = int()
        if CoinsAmount2 == ValueError:
            CoinsAmount2 = (input("Enter a number: "))

    coins -= 100



# Make it have a button to try again or quit and then make it so that winning becomes less likely,
# make the chance of the first 2 being the same higher for epicness
# la chance de double 7 est 5% mais la chance des triple 7, 0.05%
# derniere le trente jeux les chance des gagner est 30% plus basse











