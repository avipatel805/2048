import pygame as pg
import random
pg.init()

screen = pg.display.set_mode([900, 900])
screen.fill((205, 193, 181))
pg.draw.line(screen, (187, 173, 160), (0, 0), (900, 0), 40)
pg.draw.line(screen, (187, 173, 160), (0, 0), (0, 900), 40)
pg.draw.line(screen, (187, 173, 160), (900, 900), (900, 0), 40)
pg.draw.line(screen, (187, 173, 160), (0, 900), (900, 900), 40)
# 230, 450, 670
pg.draw.line(screen, (187, 173, 160), (230, 0), (230, 900), 20)
pg.draw.line(screen, (187, 173, 160), (450, 0), (450, 900), 20)
pg.draw.line(screen, (187, 173, 160), (670, 0), (670, 900), 20)
pg.draw.line(screen, (187, 173, 160), (0, 230), (900, 230), 20)
pg.draw.line(screen, (187, 173, 160), (0, 450), (900, 450), 20)
pg.draw.line(screen, (187, 173, 160), (0, 670), (900, 670), 20)

#20, 240, 460, 680
two = pg.image.load('Two.png')
four = pg.image.load('Four.png')
eight = pg.image.load('Eight.png')
sixteen = pg.image.load('Sixteen.jpg')
thirtyTwo = pg.image.load('ThirtyTwo.jpg')
sixtyFour = pg.image.load('SixtyFour.jpg')
oneTwentyEight = pg.image.load('OneTwentyEight.jpg')
twoFiftySix = pg.image.load('TwoFiftySix.png')
fiveTwelve = pg.image.load('FiveTwelve.png')
tenTwentyFour = pg.image.load('TenTwentyFour.png')
twentyFortyEight = pg.image.load('TwentyFortyEight.png')

running = True
board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


def setUp():
    board[random.randint(0, 3)][random.randint(0, 3)] = random.choice((2, 4))
    while True:
        rand1 = random.randint(0, 3)
        rand2 = random.randint(0, 3)
        if board[rand1][rand2] == 0:
            board[rand1][rand2] = random.choice((2, 4))
            break


def getPos(row, column):
    # 20, 240, 460, 680
    rowPos = 0
    columnPos = 0
    if row == 0:
        rowPos = 20
    elif row == 1:
        rowPos = 240
    elif row == 2:
        rowPos = 460
    elif row == 3:
        rowPos = 680

    if column == 0:
        columnPos = 20
    elif column == 1:
        columnPos = 240
    elif column == 2:
        columnPos = 460
    elif column == 3:
        columnPos = 680

    return columnPos, rowPos


def right(bo, add=True):
    print('right')
    filled0 = []
    for num in bo[0]:
        if num != 0:
            filled0.append(num)
    filled1 = []
    for num in bo[1]:
        if num != 0:
            filled1.append(num)
    filled2 = []
    for num in bo[2]:
        if num != 0:
            filled2.append(num)
    filled3 = []
    for num in bo[3]:
        if num != 0:
            filled3.append(num)

    for i in range(4-len(filled0)):
        filled0.insert(0, 0)
    for i in range(4-len(filled1)):
        filled1.insert(0, 0)
    for i in range(4-len(filled2)):
        filled2.insert(0, 0)
    for i in range(4-len(filled3)):
        filled3.insert(0, 0)
    nbo = [filled0, filled1, filled2, filled3]
    # combine similar nums
    if add:
        for i in range(4):
            for j in reversed(range(3)):
                if nbo[i][j] == nbo[i][j+1] and nbo[i][j] != 0:
                    print('same')
                    nbo[i][j+1] *= 2
                    nbo[i][j] = 0
                    right(nbo)
    print(nbo)
    return nbo
def left(bo, add=True):
    print('left')
    filled0 = []
    for num in bo[0]:
        if num != 0:
            filled0.append(num)
    filled1 = []
    for num in bo[1]:
        if num != 0:
            filled1.append(num)
    filled2 = []
    for num in bo[2]:
        if num != 0:
            filled2.append(num)
    filled3 = []
    for num in bo[3]:
        if num != 0:
            filled3.append(num)

    for i in range(4 - len(filled0)):
        filled0.append(0)
    for i in range(4 - len(filled1)):
        filled1.append(0)
    for i in range(4 - len(filled2)):
        filled2.append(0)
    for i in range(4 - len(filled3)):
        filled3.append(0)

    nbo = [filled0, filled1, filled2, filled3]
    # combine similar nums
    if add:
        for i in range(4):
            for j in range(3):
                if nbo[i][j] == nbo[i][j + 1] and nbo[i][j] != 0:
                    print('same')
                    nbo[i][j] *= 2
                    nbo[i][j+1] = 0
                    #left(nbo)
    print(nbo)
    return nbo


def up(bo, add=True):
    print('up')
    filled0 = []
    for row in bo:
        if row[0] != 0:
            filled0.append(row[0])
    filled1 = []
    for row in bo:
        if row[1] != 0:
            filled1.append(row[1])
    filled2 = []
    for row in bo:
        if row[2] != 0:
            filled2.append(row[2])
    filled3 = []
    for row in bo:
        if row[3] != 0:
            filled3.append(row[3])

    for i in range(4 - len(filled0)):
        filled0.append(0)
    for i in range(4 - len(filled1)):
        filled1.append(0)
    for i in range(4 - len(filled2)):
        filled2.append(0)
    for i in range(4 - len(filled3)):
        filled3.append(0)

    nbo = [[filled0[0], filled1[0], filled2[0], filled3[0]],
            [filled0[1], filled1[1], filled2[1], filled3[1]],
            [filled0[2], filled1[2], filled2[2], filled3[2]],
            [filled0[3], filled1[3], filled2[3], filled3[3]]
            ]

    # combine similar nums
    if add:
        for i in range(3):
            for j in range(4):
                if nbo[i][j] == nbo[i+1][j] and nbo[i][j] != 0:
                    print('same')
                    nbo[i][j] *= 2
                    nbo[i+1][j] = 0
                    up(nbo)
    print(nbo)
    return nbo


def down(bo, add=True):
    print('down')
    filled0 = []
    for row in bo:
        if row[0] != 0:
            filled0.append(row[0])
    filled1 = []
    for row in bo:
        if row[1] != 0:
            filled1.append(row[1])
    filled2 = []
    for row in bo:
        if row[2] != 0:
            filled2.append(row[2])
    filled3 = []
    for row in bo:
        if row[3] != 0:
            filled3.append(row[3])

    for i in range(4 - len(filled0)):
        filled0.insert(0, 0)
    for i in range(4 - len(filled1)):
        filled1.insert(0, 0)
    for i in range(4 - len(filled2)):
        filled2.insert(0, 0)
    for i in range(4 - len(filled3)):
        filled3.insert(0, 0)

    nbo = [[filled0[0], filled1[0], filled2[0], filled3[0]],
           [filled0[1], filled1[1], filled2[1], filled3[1]],
           [filled0[2], filled1[2], filled2[2], filled3[2]],
           [filled0[3], filled1[3], filled2[3], filled3[3]]
           ]

    # combine similar nums
    if add:
        for i in reversed(range(3)):
            for j in range(4):
                if nbo[i][j] == nbo[i + 1][j] and nbo[i][j] != 0:
                    print('same')
                    nbo[i+1][j] *= 2
                    nbo[i][j] = 0
                    up(nbo)

    print(nbo)
    return nbo


setUp()


def generate():
    while True:
        rand1 = random.randint(0, 3)
        rand2 = random.randint(0, 3)
        if board[rand1][rand2] == 0:
            board[rand1][rand2] = random.choice((2, 4))
            break

oldBoard = board[:]
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYUP:
            if event.key == pg.K_RIGHT:
                board = right(board)
                board = right(board, add=False)
                board = right(board, add=False)
                board = right(board, add=False)
            elif event.key == pg.K_LEFT:
                board = left(board)
                board = left(board, add=False)
                board = left(board, add=False)
                board = left(board, add=False)
            elif event.key == pg.K_UP:
                board = up(board)
                board = up(board, add=False)
                board = up(board, add=False)
                board = up(board, add=False)
            elif event.key == pg.K_DOWN:
                board = down(board)
                board = down(board, add=False)
                board = down(board, add=False)
                board = down(board, add=False)


    screen.fill((205, 193, 181))
    pg.draw.line(screen, (187, 173, 160), (0, 0), (900, 0), 40)
    pg.draw.line(screen, (187, 173, 160), (0, 0), (0, 900), 40)
    pg.draw.line(screen, (187, 173, 160), (900, 900), (900, 0), 40)
    pg.draw.line(screen, (187, 173, 160), (0, 900), (900, 900), 40)
    # 230, 450, 670
    pg.draw.line(screen, (187, 173, 160), (230, 0), (230, 900), 20)
    pg.draw.line(screen, (187, 173, 160), (450, 0), (450, 900), 20)
    pg.draw.line(screen, (187, 173, 160), (670, 0), (670, 900), 20)
    pg.draw.line(screen, (187, 173, 160), (0, 230), (900, 230), 20)
    pg.draw.line(screen, (187, 173, 160), (0, 450), (900, 450), 20)
    pg.draw.line(screen, (187, 173, 160), (0, 670), (900, 670), 20)

    for row in range(4):
        for column in range(4):
            if board[row][column] == 2:
                screen.blit(two, getPos(row, column))
            elif board[row][column] == 4:
                screen.blit(four, getPos(row, column))
            elif board[row][column] == 8:
                screen.blit(eight, getPos(row, column))
            elif board[row][column] == 16:
                screen.blit(sixteen, getPos(row, column))
            elif board[row][column] == 32:
                screen.blit(thirtyTwo, getPos(row, column))
            elif board[row][column] == 64:
                screen.blit(sixtyFour, getPos(row, column))
            elif board[row][column] == 128:
                screen.blit(oneTwentyEight, getPos(row, column))
            elif board[row][column] == 256:
                screen.blit(twoFiftySix, getPos(row, column))
            elif board[row][column] == 512:
                screen.blit(fiveTwelve, getPos(row, column))
            elif board[row][column] == 1024:
                screen.blit(tenTwentyFour, getPos(row, column))
            elif board[row][column] == 2048:
                screen.blit(twentyFortyEight, getPos(row, column))
    pg.display.flip()
    pg.time.delay(100)
    if oldBoard != board:
        generate()
    oldBoard = board[:]

    pg.display.flip()
pg.quit()