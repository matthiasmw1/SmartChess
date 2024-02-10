import serial
import time


def init_arduino(port='/dev/ttyACM0', baudrate=115200):
    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)
        print("----------Arduino verbunden!----------\n")
        return ser
    except serial.serialutil.SerialException:
        print("----------Arduino NICHT verbunden!----------\n")

def send_gcode(gcode):
    arduino.write((l + '\n').encode())
    time.sleep(0.05)
    response = arduino.readline()
    return response

    #ser.write(gcode.encode())
    #response = ser.readline().decode().strip()
    #return response

def close_arduino(ser):
    ser.close()

def read_all_lines(arduino):
    lines = []
    while arduino.in_waiting > 0:
        line = arduino.readline().decode().strip()
        lines.append(line)

    return lines

if __name__ == "__main__":
    arduino = init_arduino()

    try:
        while True:

            response_lines = read_all_lines(arduino)
            for line in response_lines:
                print(f"Antwort vom Arduino: {line}")

            gcode_command = input("G-Code eingeben: ")
            
            if gcode_command.lower() == 'exit':
                break

            send_gcode(gcode_command)
            time.sleep(1)

            response_lines = read_all_lines(arduino)
            for line in response_lines:
                print(f"Antwort vom Arduino: {line}")

            #response = send_gcode(arduino, gcode_command)
            #print(f"Antwort vom Arduino: {response}")




    except KeyboardInterrupt:
        pass
    except serial.serialutil.SerialException:
        print("----------Arduino NICHT verbunden!----------\n")
        print("Command nicht ausgeführt! Programm endet!")
        exit()
    finally:
        close_arduino(arduino)