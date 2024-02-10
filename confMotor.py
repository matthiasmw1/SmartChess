import RPi.GPIO as GPIO
import serial
import time

ser = serialS.Serial('/dev/ttyS0', 9600)

taster1 = 11
taster2 = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(taster1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(taster2, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if GPIO.input(taster1) == GPIO.LOW:
            print("Taster 1 wurde gedrückt")
            ser.write(b'T1')
        if GPIO.input(taster2) == GPIO.LOW:
            print("Taster 2 wurde gedrückt")
            ser.write(b'T2')

        time.sleep(0.1)

except KeyBoardInterrupt:
    GPIO.cleanup()