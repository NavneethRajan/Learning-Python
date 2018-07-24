def tictactoe():
    squares = []

    player1turn = True

    win = False

    for x in range (0,9):
        squares.append(str(x+1))

    def tictacboard():
        print("\n -----")
        print("|" + squares[6] + "|" + squares[7] + "|" + squares[8] + "|")
        print(" -----")
        print("|" + squares[3] + "|" + squares[4] + "|" + squares[5] + "|")
        print(" -----")
        print("|" + squares[0] + "|" + squares[1] + "|" + squares[2] + "|")
        print(" -----\n")

    while not win:
        tictacboard()

        if player1turn == True:
            print("Player 1:")
        else:
            print("Player 2:")

        try:
            playermove = int(input(">> "))
        except:
            print("This is not a valid move. Please try again.")
            continue
        
        try:
            if squares[playermove - 1] == "X" or squares[playermove - 1] == "O":
                print("Nice try but this space is already taken. Please try again!")
                continue
        except:
            print("This is not a valid move. Please try again.")
            continue

        if player1turn == True:
            squares[playermove - 1] = "X"
        else:
            squares[playermove - 1] = "O"
        
        player1turn = not player1turn

        for x in range(0, 3):
            y = x * 3
            if (squares[y] == squares[(y + 1)] and squares[y] == squares[(y + 2)]):
                win = True
                tictacboard()
            if (squares[x] == squares[(x + 3)] and squares[x] == squares[(x + 6)]):
                win = True
                tictacboard()

        if ((squares[0] == squares[4] and squares[0] == squares[8]) or
            (squares[2] == squares[4] and squares[2] == squares[6])):
            win = True
            tictacboard()

    if player1turn == True:
        print("Congratulations! Player 2 wins!!!")
    else:
        print("Congratulations! Player 1 wins!!!")

gamestart = True

while gamestart == True:
    tictactoe()
    choice = input("Do you want to play again? [y/n]: ")
    if choice == "y":
        gamestart = True
    elif choice == "n":
        gamestart = False

print("Thank you for playing!")
print("Goodbye!")
