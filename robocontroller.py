import serial
import time

def init_arduino(port='/dev/ttyACM0', baudrate=115200):
    try:
        ser = serial.Serial(port, baudrate, timeout=1)
        time.sleep(2)
        print("----------Arduino verbunden!----------\n")
        return ser
        print("----------Arduino NICHT verbunden!----------\n")

def close_arduino(ser):
    ser.close()

def read_all_lines(arduino):
    lines = []
    while arduino.in_waiting > 0:
        line = arduino.readline().decode().strip()
        lines.append(line)
    return lines

class SendGcode:
    def __init__(self, arduino):
        self.arduino = arduino

    def send_gcode(self, gcode):
        self.arduino.write((gcode + '\n').encode())
        time.sleep(0.05)
        response = self.arduino.readline().decode().strip()
        return response

if __name__ == "__main__":
    arduino = init_arduino()
    gcode_sender = SendGcode(arduino)

    try:
        while True:
            response_lines = read_all_lines(arduino)
            for line in response_lines:
                print(f"Antwort vom Arduino: {line}")

            gcode_command = input("\nG-Code eingeben: ")

            if gcode_command.lower() == 'exit':
                break

            response = gcode_sender.send_gcode(gcode_command)
            print(f"Antwort vom Arduino: {response}")

    except KeyboardInterrupt:
        print("Auf Wiedersehen!")
        exit()
    except serial.serialutil.SerialException:
        print("----------Arduino NICHT verbunden!----------\n")
        print("Command nicht ausgeführt! Programm endet!")
        exit()
    finally:
        close_arduino(arduino)
