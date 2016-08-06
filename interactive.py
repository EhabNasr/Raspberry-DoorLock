import inputInterface as UI
import ServoLock as Lock
import time

#to be replaced by Controller

while True:
    print('Please press any key to inter password: ')
    UI.getChar()
    print('Welcome!')
    Pass = UI.getPassword()
    while Pass != '2222':
        print('Wrong pin code!')
        Pass = UI.getPassword()

    Lock.openLock()
    time.sleep(5)
    Lock.closeLock()
