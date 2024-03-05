import re

def isColor(piece):
    white = re.compile('[♟♜♞♝♚♛]')
    black = re.compile('[♙♖♘♗♔♕]')

    if bool(white.search(piece)):
        return 'white'
    if bool(black.search(piece)):
        return 'black'
    else:
        return None

def printBoard():
    r = 8
    print('\n   \033[4m A  B  C  D  E  F  G  H \033[0m   ')
    for row in checkboardMap:
        print(r, end=' |')
        for col in row:
            print(f'\033[4m{col} |\033[0m', end='')
        print(f' {r}')
        r -= 1
    print('    A  B  C  D  E  F  G  H')

def translatePos(pos):
    x = pos[0]
    y = 8-int(pos[1])
    x = x.upper()

    if x == 'A':
        x = 0
    elif x == 'B':
        x = 1
    elif x == 'C':
        x = 2
    elif x == 'D':
        x = 3
    elif x == 'E':
        x = 4
    elif x == 'F':
        x = 5
    elif x == 'G':
        x = 6
    elif x == 'H':
        x = 7

    return x, y

def checkMove(pieceType, capture, From, To):
    canMove = False
    FromX, FromY = From
    ToX, ToY = To

    if pieceType == '♙':
        if not isColor(capture) == 'black' and FromY < ToY and ((FromX == ToX and not isColor(capture) == 'white' and ((ToY == FromY+1) or (ToY == FromY+2 and FromY == 1))) or (isColor(capture) == 'white' and abs(FromX - ToX) == 1 and abs(FromY - ToY))):
            canMove = True

    elif pieceType == '♟':
        if not isColor(capture) == 'white' and FromY > ToY and ((FromX == ToX and not isColor(capture) == 'black' and ((ToY == FromY-1) or (ToY == FromY-2 and FromY == 6))) or (isColor(capture) == 'black' and abs(FromX - ToX) == 1 and abs(FromY - ToY))):
            canMove = True

    elif pieceType == '♜' or pieceType == '♖':
        if ToY == FromY or ToX == FromX:
            if pieceType == '♜' and not isColor(capture) == 'white':
                canMove = True
            elif pieceType == '♖' and not isColor(capture) == 'black':
                canMove = True

    elif pieceType == '♞' or pieceType == '♘':
        if (abs(FromX-ToX) == 2 and abs(FromY-ToY) == 1) or (abs(FromY-ToY) == 2 and abs(FromX-ToX) == 1):
            if pieceType == '♞' and not isColor(capture) == 'white':
                canMove = True
            elif pieceType == '♘' and not isColor(capture) == 'black':
                canMove = True

    elif pieceType == '♝' or pieceType == '♗':
        if abs(FromX-ToX) == abs(FromY-ToY):
            if pieceType == '♝' and not isColor(capture) == 'white':
                canMove = True
            elif pieceType == '♗' and not isColor(capture) == 'black':
                canMove = True

    elif pieceType == '♚' or pieceType == '♔':
        if abs(FromX-ToX) <= 1 and abs(FromY-ToY) <= 1:
            if pieceType == '♚' and not isColor(capture) == 'white':
                canMove = True
            elif pieceType == '♔' and not isColor(capture) == 'black':
                canMove = True

    elif pieceType == '♛' or pieceType == '♕':
        if (ToY == FromY or ToX == FromX) or (abs(FromX-ToX) == abs(FromY-ToY)):
            if pieceType == '♛' and not isColor(capture) == 'white':
                canMove = True
            elif pieceType == '♕' and not isColor(capture) == 'black':
                canMove = True

    return canMove

def movePiece(From, To, Map):
    pieceX, pieceY = translatePos(From)
    toX, toY = translatePos(To)

    piece = Map[pieceY][pieceX]
    capture = Map[toY][toX]

    if checkMove(piece, capture, translatePos(From), translatePos(To)):
        Map[pieceY][pieceX] = ' '
        
        if capture == '♔':
            print('White wins!')
        elif capture == '♚':
            print('Black wins!')
        elif piece == '♙' and toY == 7:
            newPiece = input('1- ♕  2- ♖  3- ♗  4- ♘  ')
            if newPiece == '1':
                piece = '♕'
            elif newPiece == '2':
                piece = '♖'
            elif newPiece == '3':
                piece = '♗'
            elif newPiece == '4':
                piece = '♘'
        elif piece == '♟' and toY == 0:
            newPiece = input('1- ♛  2- ♜  3- ♝  4- ♞  ')
            if newPiece == '1':
                piece = '♛'
            elif newPiece == '2':
                piece = '♜'
            elif newPiece == '3':
                piece = '♝'
            elif newPiece == '4':
                piece = '♞'
            
        Map[toY][toX] = piece
        printBoard()
    else:
        return print('Error')


checkboardMap = [
    ['♖','♘','♗','♕','♔','♗','♘','♖'],
    ['♙','♙','♙','♙','♙','♙','♙','♙'],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
    ['♟','♟','♟','♟','♟','♟','♟','♟'],
    ['♜','♞','♝','♛','♚','♝','♞','♜'],
    ]

printBoard()
while True:
    a, b = input('\nfrom / to: ').split(' ')
    movePiece(a, b, checkboardMap)
