# initialize board
board = [4] * 14
pot1 = 6
pot2 = 13

# set pots to 0
board[pot1] = 0
board[pot2] = 0 
skip = False
def skip(user, pos, n, dist):
    if (user == 1 and pos + n == pot1):
        dist + 1
        return True
    if (user == 2 and pos + n == pot2):
        dist + 1
        return True
    else:
        return False
def Move(user, pos):
    dist = board[pos]
    board[pos] = 0
    for n in range(1, dist + 1):
        skipper = skip(user, pos, n, dist)
        if skipper == True:
            dist += 1
            continue
        board[n] += 1
        if ((pos + n) > len(board)):
            for k in range(0, (dist + 1 - n)):
                skipper = skip(user, pos, n, dist)
                if skipper == True:
                    dist += 1
                    continue
                board[k] += 1
        board[pos + n] += 1
for x in range(0, 10):
    Move(1, 2)
    print(board)
