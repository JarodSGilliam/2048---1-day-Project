import random

# print("hi")
game = [[0, 0, 0, 0],[2, 2, 2, 8],[0, 0, 0, 0],[0, 0, 0, 0]]

def maxVal():
    max = 0
    for a in game:
        for b in a:
            if b > max:
                max = b
    return max

def addBlock(number):
    while True:
        a = random.randint(0,3)
        b = random.randint(0,3)
        if (game[a][b] != 0):
            continue
        game[a][b] = number
        return

def gameOver():
    for a in game:
        for b in a:
            if b == 0:
                return False
                print(b)
    return True

def twoOrFour():
    if (random.randint(0,4) == 0):
        return 4
    return 2

def squish(array):
    for i in range(4):
        try:
            array.remove(0)
        except:
            break
    for i in range(len(array)):
        if i == len(array)-1:
            break
        if array[i] == array[i+1]:
            array[i] = 2*array[i]
            array[i+1] = 0
    for i in range(4):
        try:
            array.remove(0)
        except:
            break
    out = []
    for a in array:
        out.append(a)
    return out

def reverseArray(array):
    array.reverse()
    return array

# print(squish([2,0,2,4]))

def getColumn(number):
    output = [0,0,0,0]
    for i in range(4):
        output[i] = game[i][number]
    return output

def setColumn(number, array):
    for i in range(4):
        game[i][number] = array[i]


# # print(game)
# # for a in game:
# #     print(squish(a))
# right()
# # print(game)



def left():
    for row in range(4):
        temp = squish(game[row])
        while len(temp) < 4:
            temp.append(0)
        game[row] = temp


def right():
    for row in range(4):
        temp = squish(reverseArray(game[row]))
        while len(temp) < 4:
            temp.append(0)
        temp.reverse()
        game[row] = temp

def up():
    for i in range(4):
        temp = squish(getColumn(i))
        while len(temp) < 4:
            temp.append(0)
        setColumn(i, temp)

def down():
    for i in range(4):
        temp = squish(reverseArray(getColumn(i)))
        while len(temp) < 4:
            temp.append(0)
        temp.reverse()
        setColumn(i, temp)

# print(game)
# left()
# up()
# print(game)
# game[1] = [2,2,2,8]
# right()
# print(game)

addBlock(twoOrFour())
maxVal = 0
while maxVal < 49:
    for a in game:
        print(a)
    move = input("/\\ or \\/ or <- or -> as w s a d\n")
    if (move == "w"):
        up()
    if (move == "s"):
        down()
    if (move == "a"):
        left()
    if (move == "d"):
        right()
    if gameOver():
        print("No more open spaces!")
        print("Lost")
        break
    addBlock(twoOrFour())
    maxVal += 1
