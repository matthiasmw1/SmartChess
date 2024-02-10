import serial
import time

s = serial.Serial('COM13', 115200)

s.write(b"\r\n\r\n")
time.sleep(2)   
s.flushInput()  

while True:
    gcodeInput = input("G-Code Command: ")
    s.write((gcodeInput + '\n').encode())

    grbl_out = s.readline().decode()
    print(' : ' + grbl_out.strip())

    if gcodeInput == "exit":
        s.close()
        exit()