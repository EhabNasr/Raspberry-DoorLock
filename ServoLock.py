import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
p = GPIO.PWM (12, 50)
p.start(0)

CLOSE_LOCK_DUTY_CYCLE = 2.5
OPEN_LOCK_DUTY_CYCLE = 7.5

isOpen = False

def openLock():
    p.start(OPEN_LOCK_DUTY_CYCLE)
    time.sleep(0.5)
    p.start(0)
    isOpen = True
    return

def closeLock():
    p.start(CLOSE_LOCK_DUTY_CYCLE)
    time.sleep(0.5)
    p.start(0)
    isOpen = False
    return

def isOpen():
    return isOpen
