import TicTacToe as game
import random


def main():
    # choosing team
    print("Hallo, wilkommen bei TicTacToe! Wähle dein Team (X oder 0): ")
    while True:
        player = input()
        if player.lower() == "x":
            computer = "O"
            break
        if player.lower() == "o":
            computer = "X"
            break
        else:
            print("Das ist keine gültige Eingabe! Wähle X oder O aus: ")
            continue
    print("Alles klar, du hast {} gewählt! Dann ermitteln wir nun, welches Team das Spiel eröffnet: ".format(player))
    # choosing who starts
    if round(random.random()) == 0:
        beginner = player
        second = computer
    else:
        beginner = computer
        second = player
    t = game.TicTacToe()
    turn = 0
    won = False
    while turn < 9:
        # calling whose turn it is
        if turn % 2 == 0:
            print("{} ist am Zug".format(beginner))
        else:
            print("{} ist am Zug". format(second))
        # printing board
        t.out()
        # checking for win conditions
        if t.winH() or t.winD() or t.winV():
            won = True
            break
        # get position
        while True:
            try:
                pos = int(input("Position: "))
                if pos < 10 and t.board[pos - 1] == "-":
                    break
                else:
                    t.out()
                    print("Feld belegt oder keine gültige Angabe.")
            except ValueError:
                print("Ungültige Eingabe!")
                continue

        if turn % 2 == 0:
            t.set(pos - 1, beginner)
        else:
            t.set(pos - 1, second)
        turn += 1

    if won:
        print("Glückwunsch, {}  hat gewonnen!!".format(t.winner))
    else:
        print("Es konnte keiner die Partie für sich entscheiden...")


if __name__ == "__main__":
    main()
