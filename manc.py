board = [[4] * 8] * 2 
board[0][0] = 0
board[0][7] = 0
board[1][0] = 0
board[1][7] = 0
positions = ["", 1,2,3,4,5,6,""]

# Player 1 now has the ability to move pieces on its own side of the board
player1 = True
if (player1):
    side = board[0]
    print(side)
    print(positions)
    # attempt to get user input
    try:
        pos = int(input("choose which rocks you would like to move:"))
        print("You chose ", pos)
    except ValueError:
        print("Please enter a positive integer between 1 and 7")
    
    # move rocks across users side of board
    rocks = side[pos]
    side[pos] = 0
    for n in range(1, rocks + 1):
      side[pos+n] += 1

    print(board[0])
        