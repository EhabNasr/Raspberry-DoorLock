import I2C_LCD_driver
import keypad
import time


mylcd = I2C_LCD_driver.lcd()
kp = keypad.keypad()

def getPassword():
    password = ''
    while len(password) < 4:
        char = getChar()
        password += str(char)
        mylcd.lcd_display_string(('password' + '    '), 2, 0)
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




def main():
    On_Hold_Message()
    kp.getChar()
    Welcome_Message()
    Receiving_Pin_Code_Message()
    Pass = kp.getPassword()


main()