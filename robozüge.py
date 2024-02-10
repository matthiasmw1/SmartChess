import serial
import time
import chess
import chess.engine
import RPi.GPIO as GPIO
from time import sleep
from stockfish import Stockfish
from robocontroller import *  # Import class/def from file

# init Arduino
s = init_arduino()

s.write(b"\r\n\r\n") # wake up machine
time.sleep(2)
s.flushInput # delete input

# init elektromagent
GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)

# init stockfish
board = chess.Board()
print(board, "\n")
#stockfish_path = "C:\\Users\\Mohamad\\Desktop\\Diplomarbeit\\stockfish\\stockfish-windows-x86-64-avx2.exe"
stockfish_path = "/home/matthias/Diplomarbeit/stockfish-engine/stockfish-ubuntu-x86-64-avx2"
stockfish = Stockfish(path=stockfish_path)
schwierigkeitsstufe = 10


def display_object(matrix, row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
        print(matrix[row][col])

    else:
        print("Invalid row or column index.")

def generate_gcode(x1, y1, x2, y2):
    return f"G0 X{x1} Y{y1}\nG0 X{x2} Y{y2}\n"

def elektromagent(status):
    if status == HIGH:
        GPIO.output(14, GPIO.HIGH)
    if status == LOW:
        GPIO.output(14, GPIO.LOW)


# Chessmatrix
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




if __name__ == "__main__":
    with chess.engine.SimpleEngine.popen_uci(stockfish_path) as engine:
        while not board.is_game_over():
            try:
                if board.turn == chess.WHITE:   # Spieler
                    user_move = input("Gib den Zug ein (z.B., a2a4): ")
                    move = chess.Move.from_uci(user_move)
                    if move in board.legal_moves:
                        board.push(move)
                    else: 
                        print("Ungültiger Zug!")
                else:   # Schachengine
                    result = engine.play(board, chess.engine.Limit(time=0.1))
                    print("\n", result.move)
                    board.push(result.move)
                        
                                    
                    print(board)
                    # Schachroboter
                    # Eingabezeile und Spalte
                    input_str = str(result.move) #input("Gib den Zug ein (z.B., a2a4): ")  input from chessrobo
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


                    # generate G-Code
                    # -!-!-!- Verbesserungspotenial -!-!-!-
                    gcode = generate_gcode(O_x, O_y, N_x, N_y)
                    print("Generierter G-Code:")
                    print(gcode)

                    gcode = gcode.split('\n')

                    print(SendGcode(gcode[0]))
                    time.sleep(5)
                    print("Figur angezogen")
                    # Schachfigur anziehen

                    print(SendGcode(gcode[1]))
                    time.sleep(5)
                    print("Figur losgelassen")
                    # Schachfigur loslassen

                    print(SendGcode('G0 X0 Y0'))
                    print("Ausgangsposition")


                    #print(type(gcode))
                    #time.sleep(1)
                    #s.write(("$X").encode())
                    #time.sleep(1)
                    #s.write((gcode).encode())


            except KeyboardInterrupt:
                exit()
