import serial
import time

s = serial.Serial('/dev/ttyACM0', 115200)

s.write(b"\r\n\r\n")
time.sleep(2)
s.flushInput()

def display_object(matrix, row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
        print(matrix[row][col])

    else:
        print("Invalid row or column index.")

def generate_gcode(x1, y1, x2, y2):
    return f"G0 X{x1} Y{y1}\nG1 X{x2} Y{y2}\n"

# Beispielmatrizen
matrix = [
    ["BT","BH","BL","BQ","BK","BL","BH","BT"],
    ["BP","BP","BP","BP","BP","BP","BP","BP"],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ["WP","WP","WP","WP","WP","WP","WP","WP"],
    ["WT","WH","WL","WQ","WK","WL","WH","WT"]
]

matrix2 = [
    [f"x={10 + i} y={65 + j}" for i in range(8)] for j in range(8)
]

# Eingabezeile und Spalte
input_str = input("Gib den Zug ein (z.B., a2a4): ")
O_row_input = int(input_str[1]) - 1
O_col_input = "abcdefgh".index(input_str[0].lower())
N_row_input = int(input_str[3]) - 1
N_col_input = "abcdefgh".index(input_str[2].lower())

display_object(matrix, O_row_input, O_col_input)
display_object(matrix2, O_row_input, O_col_input)
display_object(matrix2, N_row_input, N_col_input)

# Extrahiere Koordinaten aus matrix2
O_coordinates = matrix2[O_row_input][O_col_input]
N_coordinates = matrix2[N_row_input][N_col_input]

# Extrahiere x und y Werte
O_x, O_y = map(int, [coord.split('=')[1] for coord in O_coordinates.split() if 'x=' in coord or 'y=' in coord])
N_x, N_y = map(int, [coord.split('=')[1] for coord in N_coordinates.split() if 'x=' in coord or 'y=' in coord])



# Generiere G-Code
gcode = generate_gcode(O_x, O_y, N_x, N_y)
print("Generierter G-Code:")
print(gcode)
time.sleep(1)
s.write(("$X").encode())
time.sleep(1)
s.write((gcode).encode())

# Die folgenden Zeilen zur Verbindung mit Arduino und zum Senden von G-Code müssen noch entkommentiert werden
# s = serial.Serial('/dev/ttyACM0', 115200)
# s.write(b"\r\n\r\n")
# time.sleep(2)
# s.flushInput()
# s.write(gcode.encode())
