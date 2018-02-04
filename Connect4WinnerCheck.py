def SlopeDown(x, y):
    return x + 1, y - 1

def SlopeUp(x, y):
    return x - 1, y - 1

def Row(x, y):
    return x + 1, y

def Col(x, y):
    return x, y + 1

def Check(x, y, board, player, path):
    width = len(board[0])
    height = len(board)

    for _ in range(4):
        if (x >= width) or (x < 0):
            return False
        if (y >= height) or (y < 0):
            return False
        if (board[y][x] != player):
            return False
        x, y = path(x, y)

    return True

def IsWinner(board, player):
    width = len(board[0])
    height = len(board)

    paths = [SlopeDown, SlopeUp, Row, Col]
    for y in range(height):
        for x in range(width):
            for path in paths:
                if Check(x, y, board, player, path):
                    return True
    return False

board = [
            [' ',' ',' ',' ',' ',' ','B'],
            ['B','B',' ',' ','G',' ',' '],
            [' ',' ','B','B',' ',' ',' '],
            [' ',' ','B',' ',' ',' ',' '],
            [' ','B','B',' ',' ','B',' '],
            [' ',' ',' ',' ',' ',' ',' '],
        ]
print '----'
print IsWinner (board, 'G')
print IsWinner (board, 'B')

board = [
            [' ',' ',' ','G','G','G','G'],
            ['B','B',' ',' ','G',' ',' '],
            [' ',' ','B','B',' ','B','B'],
            ['B','B','B',' ',' ',' ',' '],
            [' ','B','B',' ',' ','B',' '],
            [' ',' ',' ',' ',' ',' ',' '],
        ]
print '----'
print IsWinner (board, 'G')
print IsWinner (board, 'B')

board = [
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ','B',' ',' ',' ',' '],
            [' ',' ',' ','B',' ',' ',' '],
            [' ',' ',' ',' ','B',' ',' '],
            [' ',' ',' ',' ',' ','B',' '],
            [' ',' ',' ',' ',' ',' ',' '],
        ]
print '----'
print IsWinner (board, 'G')
print IsWinner (board, 'B')

board = [
            [' ',' ',' ',' ',' ',' ',' '],
            [' ',' ','B',' ','G',' ',' '],
            [' ',' ',' ','G',' ',' ',' '],
            [' ',' ','G',' ','B',' ',' '],
            [' ','G',' ',' ',' ','B',' '],
            [' ',' ',' ',' ',' ',' ',' '],
        ]
print '----'
print IsWinner (board, 'G')
print IsWinner (board, 'B')