import keypad
import time


kp = keypad.keypad()

def getPassword():
    password = ''
    print('enter pin code: ')
    while len(password) < 4:
        char = getChar()
        password = password + str(char)
        print(password)
    return password

def getChar():
    digit = None
    while digit == None:
        digit = kp.getKey()
        time.sleep(0.2)
    return digit

