import chess.engine

stockfish_path = "/home/matthias/Diplomarbeit/stockfish-engine/stockfish-ubuntu-x86-64-avx2"



def main():

    with chess.engine.SimpleEngine.popen_uci(stockfish_path) as engine:
        board = chess.Board()   # Schachbrett wird erstellt
        engine.configure({"Skill Level": 7})    # Schwierigkeit wird eingestellt
        result = engine.play(board, chess.engine.Limit(time=0.1))   # Berechnung des nächsten Schritts
        print("Bester Zug: ", result.move)

if __name__ == "__main__":
    main()
    