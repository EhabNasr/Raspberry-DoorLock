import RPi.GPIO as GPIO

RED   = 22
BLUE  = 18
GREEN = 16

GPIO.setmode(GPIO.BOARD)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)

def switchOff():
    GPIO.output(RED, GPIO.HIGH)
    GPIO.output(BLUE, GPIO.HIGH)
    GPIO.output(GREEN, GPIO.HIGH)
    return

def switchBlue():
    GPIO.output(RED, GPIO.HIGH)
    GPIO.output(GREEN, GPIO.HIGH)
    GPIO.output(BLUE, GPIO.LOW)
    return

def switchGreen():
    GPIO.output(RED, GPIO.HIGH)
    GPIO.output(BLUE, GPIO.HIGH)
    GPIO.output(GREEN, GPIO.LOW)
    return

def switchRed():
    GPIO.output(GREEN, GPIO.HIGH)
    GPIO.output(BLUE, GPIO.HIGH)
    GPIO.output(RED, GPIO.LOW)
    return
