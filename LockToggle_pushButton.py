import RPi.GPIO as GPIO
import time
import ServoLock as Lock

GPIO.setmode(GPIO.BOARD)

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def checkInput():
    if GPIO.input(24):
        return False
    else:
        time.sleep(0.5)
        return (not GPIO.input())
    return


def toggleState():
    if Lock.isOpen():
        Lock.closeLock()
    else:
        Lock.openLock()


