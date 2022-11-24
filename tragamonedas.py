import random
import time
import os
import keyboard
import pdb
print()
print('''Welcome to the Slot Machine 
You'll start with £50. You'll be asked if you want to play.
Answer with yes/no. you can also use y/n
There is no case sensitivity, type it however you like!
To win you must get one of the following combinations:
BAR\tBAR\tBAR\t\tpays\t£250
BELL\tBELL\tBELL/BAR\tpays\t£20
PLUM\tPLUM\tPLUM/BAR\tpays\t£14
ORANGE\tORANGE\tORANGE/BAR\tpays\t£10
CHERRY\tCHERRY\tCHERRY\t\tpays\t£7
CHERRY\tCHERRY\t  -\t\tpays\t£5
CHERRY\t  -\t  -\t\tpays\t£2
7\t  7\t  7\t\tpays\t The Jackpot!
''')
time.sleep(3)
#Constants:
INIT_STAKE = 50
INIT_BALANCE = 1000
ITEMS = ["CHERRY", "LEMON", "ORANGE", "PLUM", "BELL", "BAR", "7"]

firstWheel = None
secondWheel = None
thirdWheel = None
stake = INIT_STAKE
balance = INIT_BALANCE

def play():
    global stake, firstWheel, secondWheel, thirdWheel
    playQuestion = askPlayer()
    slots = [firstWheel, secondWheel, thirdWheel]
    while(stake != 0 and playQuestion == True):
        ciclo = 0
        while ciclo != 3:
            for i in range(ciclo, 3, 1):
                slots[i] = spinWheel()
            print(slots[0] + '\t' + slots[1] + '\t' + slots[2])
            time.sleep(.22)
            os.system('cls' if os.name == 'nt' else 'clear')
            if keyboard.is_pressed("a"):
                ciclo += 1
                
        printScore(slots)        
        playQuestion = askPlayer()

def askPlayer():
    '''
    Asks the player if he wants to play again.
    expecting from the user to answer with yes, y, no or n
    No case sensitivity in the answer. yes, YeS, y, y, nO . . . all works
    '''
    global stake
    global balance
    while(True):
        os.system('cls' if os.name == 'nt' else 'clear')
        if (balance <=1):
            print ("Machine balance reset.")
            balance = 1000

        print ("The Jackpot is currently: £" + str(balance) + ".")
        print ("You currently have £" + str(stake) + ".")
        answer = input("Would you like to play?")
        answer = answer.lower()
        if(answer == "yes" or answer == "y"):
            return True
        elif(answer == "no" or answer == "n"):
            print("\nYou ended the game with £" + str(stake) + " in your hand.")
            time.sleep(2)
            return False
        else:
            print("Whoops! Didn't get that.")

def spinWheel():
    '''
    returns a random item from the wheel
    '''
    randomNumber = random.randint(0, 5)
    return ITEMS[randomNumber]

def printScore(slots):
    '''
    prints the current score
    '''
    global stake, balance
    if((slots[0] == "CHERRY") and (slots[1] != "CHERRY")):
        win = 2
        balance = balance - 2
    elif((slots[0] == "CHERRY") and (slots[1] == "CHERRY") and (slots[2] != "CHERRY")):
        win = 5
        balance = balance - 5
    elif((slots[0] == "CHERRY") and (slots[1] == "CHERRY") and (slots[2] == "CHERRY")):
        win = 7
        balance = balance - 7
    elif((slots[0] == "ORANGE") and (slots[1] == "ORANGE") and ((slots[2] == "ORANGE") or (slots[2] == "BAR"))):
        win = 10
        balance = balance - 10
    elif((slots[0] == "PLUM") and (slots[1] == "PLUM") and ((slots[2] == "PLUM") or (slots[2] == "BAR"))):
        win = 14
        balance = balance - 14
    elif((slots[0] == "BELL") and (slots[1] == "BELL") and ((slots[2] == "BELL") or (slots[2] == "BAR"))):
        win = 20
        balance = balance - 20
    elif((slots[0] == "BAR") and (slots[1] == "BAR") and (slots[2] == "BAR")):
        win = 250
        balance = balance - 250
    elif((slots[0] == "7") and (slots[1] == "7") and (slots[2] == "7")):
        win = balance
        balance = balance - win
    else:
        win = -1
        balance = balance + 1

    stake += win
    if win == balance:
        print ("You won the JACKPOT!!")
    if(win > 0):
        print(slots[0] + '\t' + slots[1] + '\t' + slots[2] + ' -- You win £' + str(win))
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print(slots[0] + '\t' + slots[1] + '\t' + slots[2] + ' -- You lose')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

play()