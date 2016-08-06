import I2C_LCD_driver
import keypad
import time
import ServoLock as Lock

mylcd = I2C_LCD_driver.lcd()
kp = keypad.keypad()
RightPass = '2222'

def getPassword():
    password = ''
    while len(password) < 4:
        char = getChar()
        if char == '*':
            password = password[:-1]
        else:
            password += str(char)
        mylcd.lcd_display_string((password + '    '), 2, 0)
        print(password)
    return password

def getChar():
    digit = None
    while digit == None:
        digit = kp.getKey()
        time.sleep(0.2)
    return digit


def On_Hold_Message():
    print('Please Press Any Key to Start: ')
    mylcd.lcd_clear()
    mylcd.lcd_display_string('Please Press', 1)
    mylcd.lcd_display_string('Any Key to Start: ', 2, 0)


def Welcome_Message():
    print('Welcome!')
    mylcd.lcd_clear()
    mylcd.lcd_display_string('Welcome!', 1)
    time.sleep(2)

def Receiving_Pin_Code_Message():
    print('Enter Pin Code: ')
    mylcd.lcd_clear()
    mylcd.lcd_display_string('Enter Pin Code:', 1)

def Error_Message():
    mylcd.lcd_clear()
    print('Wrong Pin Code!')
    mylcd.lcd_clear()
    mylcd.lcd_display_string('Wrong Pin Code!', 1)


#  Three times wrong
def Warning_With_Message():
    mylcd.lcd_clear()
    mylcd.lcd_display_string('Warning!', 1, 5)
    mylcd.lcd_display_string('You Have to Wait', 2, 0)
    time.sleep(10)

def main():
    while True:
        Pass = ''
        numberOfTries = 0
        Lock.closeLock()
        On_Hold_Message()
        getChar()
        Welcome_Message()
        while (numberOfTries < 3) and not (Lock.isOpen()):
            Receiving_Pin_Code_Message()
            Pass = getPassword()
            if Pass == RightPass :
                Lock.openLock()
                time.sleep(5)
                Lock.closeLock()
            else:
                Error_Message()
                numberOfTries += 1
        if numberOfTries >= 3 :
            Warning_With_Message()


main()
