import chess
import chess.engine
from stockfish import Stockfish

def main():

    stockfish_path = "/home/matthias/Diplomarbeit/stockfish-engine/stockfish-ubuntu-x86-64-avx2"

    board = chess.Board()
    print(board)


    with chess.engine.SimpleEngine.popen_uci(stockfish_path) as engine:
        while not board.is_game_over():
            try:
                if board.turn == chess.WHITE:
                    user_move = input("Ihr Zug: ")
                    move = chess.Move.from_uci(user_move)
                    if move in board.legal_moves:
                        board.push(move)
                    else:
                        print("Ungültiger Zug. Versuchen Sie es erneut.")
                else:
                    result = engine.play(board, chess.engine.Limit(time=0.1))
                    board.push(result.move)

                print(board)
            except KeyboardInterrupt:
                print("\nSpiel beendet.")
                break

if __name__ == "__main__":
    main()