import serial
import time

def init_arduino(port='/dev/ttyACM0', baudrate=115200):
    ser = serial.Serial(port, baudrate, timeout=1)
    time.sleep(2)  # Wartezeit für die Arduino-Initialisierung
    return ser

def send_gcode(ser, gcode):
    ser.write(gcode.encode())
    response = ser.readline().decode().strip()
    return response

def close_arduino(ser):
    ser.close()

if __name__ == "__main__":
    arduino = init_arduino()

    try:
        while True:
            gcode_command = input("G-Code eingeben ('exit' zum Beenden): ")
            
            if gcode_command.lower() == 'exit':
                break

            response = send_gcode(arduino, gcode_command)
            print(f"Antwort vom Arduino: {response}")

    except KeyboardInterrupt:
        pass

    finally:
        close_arduino(arduino)
