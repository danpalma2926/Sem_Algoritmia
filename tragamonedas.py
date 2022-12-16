import random, time, os, keyboard
import pdb

APUESTA_INICIAL = 50
BALANCE_INICIAL = 1000
OPCIONES = ["CEREZ", "LIMON", "NARAN", "CIRUE", "CAMP", "BAR", "7"]

ruleta1, ruleta2, ruleta3 = None, None, None
fondos = APUESTA_INICIAL
balance = BALANCE_INICIAL

def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

def imprimirReglas():
    os.system('cls')
    print('''
    TRAGA MONEDAS
    Combinaciones Ganadoras:
    BAR\t\tBAR\t\tBAR\t\tgana\t$250
    CAMP\tCAMP\tCAMP/BAR\tgana\t$20
    CIRUE\tCIRUE\tCIRUE/BAR\tgana\t$14
    NARAN\tNARAN\tNARAN/BAR\tgana\t$10
    CEREZ\tCEREZ\tCEREZ\t\tgana\t$7
    CEREZ\tCEREZ\t  -\t\tgana\t$5
    CEREZ\t  -\t  -\t\tgana\t$2
    7\t  7\t  7\t\tgana\t\t El premio mayor!
    ''')
    time.sleep(6)

def main():
    global fondos, ruleta1, ruleta2, ruleta3
    imprimirReglas()
    opc = menu()
    slots = [ruleta1, ruleta2, ruleta3]
    while(fondos != 0 and opc == True):
        ciclo = 0
        while ciclo != 3:
            for i in range(ciclo, 3, 1):
                slots[i] = ruleta()
            print(slots[0] + '\t' + slots[1] + '\t' + slots[2])
            time.sleep(.18)
            os.system('cls')
            if keyboard.is_pressed("a"):
                ciclo += 1
                
        imprimirPuntaje(slots)  
        flush_input()      
        opc = menu()

def menu():
    global fondos
    global balance
    while(True):
        os.system('cls')
        if (balance <=1):
            print ("Volviendo a agregar fondos.")
            balance = 1000

        print("El premio mayor es: $" + str(balance) + ".")
        print("Actualmente tiene $" + str(fondos) + ".")
        print("'s' o 'si' para continuar jugando")
        print("'n' o 'no' para salir del programa")
        print("'r' o 'reglas' para visualizar las reglas dej juego")
        answer = input("Opcion: ")
        answer = answer.lower()
        if(answer == "si" or answer == "s"):
            return True
        elif(answer == "no" or answer == "n"):
            print("\nHas terminado el juego con $" + str(fondos))
            time.sleep(2)
            return False
        elif(answer == "reglas" or answer == "r"):
            imprimirReglas()
        else:
            print("Opcion no valida!.")
            time.sleep(2)
def ruleta():
    randomNumber = random.randint(0, 6)
    return OPCIONES[randomNumber]

def imprimirPuntaje(slots):
    global fondos, balance
    if((slots[0] == "CEREZ") and (slots[1] != "CEREZ")):
        win = 2
        balance = balance - 2
    elif((slots[0] == "CEREZ") and (slots[1] == "CEREZ") and (slots[2] != "CEREZ")):
        win = 5
        balance = balance - 5
    elif((slots[0] == "CEREZ") and (slots[1] == "CEREZ") and (slots[2] == "CEREZ")):
        win = 7
        balance = balance - 7
    elif((slots[0] == "NARAN") and (slots[1] == "NARAN") and ((slots[2] == "NARAN") or (slots[2] == "BAR"))):
        win = 10
        balance = balance - 10
    elif((slots[0] == "CIRUE") and (slots[1] == "CIRUE") and ((slots[2] == "CIRUE") or (slots[2] == "BAR"))):
        win = 14
        balance = balance - 14
    elif((slots[0] == "CAMP") and (slots[1] == "CAMP") and ((slots[2] == "CAMP") or (slots[2] == "BAR"))):
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

    fondos += win
    if win == balance:
        print ("Haz ganado el premio mayor!!")
    if(win > 0):
        print(slots[0] + '\t' + slots[1] + '\t' + slots[2] + ' -- Ganaste $' + str(win))
        time.sleep(3)
        os.system('cls')
    else:
        print(slots[0] + '\t' + slots[1] + '\t' + slots[2] + ' -- Has perdido')
        time.sleep(2)
        os.system('cls')

main()