def play():
    position = (0, 0)
    alive = True

    while position:

        if position == (0, 0):
            print("You are in a maze of twisty passages all alike.")
        elif position == (1, 0):
            print("You are on a road in a dark forest. To the north you can see a tower.")
        else:
            print("There is nothing here.")

        command = input()

        i, j = position
        if command == "N":
            position = (i, j + 1)
        elif command == "E":
            position = (i + 1, j)
        elif command == "W":
            position = (i -1, j)
        elif command == "L":
            pass
        elif command == "O":
            position = None
        else:
            print("I don't understand")

    print("Game over")


if __name__ == '__main__':
    play()

