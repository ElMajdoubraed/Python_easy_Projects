import random

board = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' ',
}

winner = ""

while True:
    player = input('select x or o : ')
    if player == 'x' or player == 'o':
        break

if player == 'x':
    computer = 'o'
else:
    computer = 'x'


def checkLine(slot1, slot2, slot3):
    if '_' in slot1 or '_' in slot2 or '_' in slot3:
        return False
    else:
        if slot1 == slot2 == slot3:
            return True
        else:
            return False


def checkWinner(board):

    return checkLine(board['1'], board['2'], board['3']) or checkLine(board['4'], board['5'], board['6']) or checkLine(board['7'], board['8'], board['8']) or checkLine(board['1'], board['4'], board['7']) or checkLine(board['2'], board['5'], board['8']) or checkLine(board['3'], board['6'], board['9']) or checkLine(board['1'], board['5'], board['9']) or checkLine(board['3'], board['5'], board['7'])


def printGameBoard(board):

    newBoard = board
    for k, v in board.items():
        if v == ' ':
            newBoard[k] = '_'

    print(newBoard['1'], newBoard['2'], newBoard['3'])
    print(newBoard['4'], newBoard['5'], newBoard['6'])
    print(newBoard['7'], newBoard['8'], newBoard['9'])


options = [*range(1, 10)]

for i in range(9):
    printGameBoard(board)

    while True:
        print('Free slots = ', options)
        choice = input('What is your choice')
        if int(choice) in options:
            break
    options.remove(int(choice))
    board[str(choice)] = player

    if checkWinner(board) == True:
        winner = 'player'
        break

    computerChoice = random.choice(options)
    options.remove(int(computerChoice))
    board[str(computerChoice)] = computer

    if checkWinner(board) == True:
        winner = 'computer'
        break

    if len(options) == 1:
        break


printGameBoard(board)

if winner != '':
    print('Ther winner is ', winner)

else:
    print('No winners')
