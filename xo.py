# TODO (1/4)
def getEmptyBoard(size):
    pass

# TODO (2/4)
def getNextPlayer(player):
    pass

def getIndex(size, row, col):
    return (row-1) * size + col - 1

def extractRow(board, size, row):
    return board[(row-1)*size : (row-1)*size+size]

def extractCol(board, size, col):
    return board[col-1 : len(board) : size]

def extractLeadDiagonal(board, size):
    return board[:: size+1]

def extractLesserDiagonal(board, size):
    return board[size-1 : len(board)-1 : size-1]

# TODO (3/4)
def getPlayerView(player):
    pass

def getSeparator(size):
    view = '-+' * (size-1) + '-'
    return view

def getRowRepr(board, size, row):
    view = ''
    row_data = extractRow(board, size, row)
    for i in row_data[:-1]:
        view = view + getPlayerView(i) + '|'
    view = view + getPlayerView(row_data[-1])
    return view

def getBoardRepr(board, size):
    view = ''
    for i in range(1, size):
        view = view + getRowRepr(board, size, i) + '\n' + getSeparator(size) + '\n'
    view = view + getRowRepr(board, size, size) + '\n'
    return view

# TODO (4/4)
def countDistinct(the_list):
    pass

def hasOneDistinct(the_list):
    return countDistinct(the_list) == 1

def getSubsequenceWinner(subsequence):
    if hasOneDistinct(subsequence):
        return subsequence[0]
    else:
        return -1

def getSubsequences(sequence, size):
    subsequences = []
    for i in range(size, len(sequence)+1):
        subsequences.append(sequence[i-size:i])
    return subsequences

def getSequences(board, size):
    seqs = []
    for i in range(1, size+1):
        seqs.append(extractRow(board, size, i))
        seqs.append(extractCol(board, size, i))
    return seqs

def getBoardSubsequences(board, size, sequence_size):
    seqs = getSequences(board, size)
    subs = []
    for seq in seqs:
        for sub in getSubsequences(seq, sequence_size):
            subs.append(sub)
    return subs

def getWinner(board, size, sequence_size):
    for sub in getBoardSubsequences(board, size, sequence_size):
        winner = getSubsequenceWinner(sub)
        if winner != -1:
            return winner
    return -1

def insertMove(board, size, player, row, col):
    if row < 1 or row > size or col < 1 or col > size:
        return False
    if board[getIndex(size, row, col)] != -1:
        return False
    board[getIndex(size, row, col)] = player
    return True

def main():
    size = 3
    board = getEmptyBoard(size)
    seq_size = 3
    player = 0
    winner = getWinner(board, size, seq_size)
    while winner == -1:
        print(getBoardRepr(board, size))
        print('Player:', getPlayerView(player))
        row = int(input('Enter row: '))
        col = int(input('Enter col: '))
        is_possible = insertMove(board, size, player, row, col)
        if not is_possible:
            print('Cannot play there')
        else:
            player = getNextPlayer(player)
        winner = getWinner(board, size, seq_size)
    print(getPlayerView(winner), 'is the winner!!!')

if __name__ == '__main__':
    main()
