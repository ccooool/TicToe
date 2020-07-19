from tictactoe_engine import play
import sys
##change

if __name__ == "__main__":
    while 1:
        try:
            player_1 = str(input("Enter Player 1's name:"))
            player_2 = str(input("Enter Player 2's name:"))
            break
        except KeyboardInterrupt:
            sys.exit()
        except:
            print("invalid name input, enter player names again")
    play(player_1, player_2)
    