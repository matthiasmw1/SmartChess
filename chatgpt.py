import chess
import chess.engine

def main():
    board = chess.Board()
    
    print("Willkommen zum Schachspiel!")
    print(board)
    
    stockfish_path = "/home/matthias/Diplomarbeit/stockfish-engine/stockfish-ubuntu-x86-64-avx2"
    schwierigkeitsstufe = 10  # Schwierigkeitsstufe (kann angepasst werden)

    with chess.engine.SimpleEngine.popen_uci(stockfish_path) as engine:
        while not board.is_game_over():
            try:
                if board.turn == chess.WHITE:
                    user_move = input("Ihr Zug (Beispiel: e2e4): ")
                    move = chess.Move.from_uci(user_move)
                    if move in board.legal_moves:
                        board.push(move)
                    else:
                        print("Ungültiger Zug. Versuchen Sie es erneut.")
                else:
                    result = engine.play(board, chess.engine.Limit(time=0.1))
                    print(type(result.move))
                    print(type(result.move))
                    print(type(input("Testzug: ")))
                    testVar = str(result.move)
                    print(type(testVar))
                    print(testVar)
                    board.push(result.move)
                    

                print(board)
            except KeyboardInterrupt:
                print("\nSpiel beendet.")
                break

if __name__ == "__main__":
    main()