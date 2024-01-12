import os
import math
import pdb
import sys

def comKeys(key1, key2):
    return f"{key1}|{key2}"

def genSpaces(maxLen, lenNum):
    spaces = []
    for x in range(maxLen - lenNum):
        spaces.append(" ")

    return "".join(spaces)

def genSquare(size, numbers, file):
    if len(numbers) != size * size:
        quit("numbersList is the wrong size")
    spaces = []
    dashes = []
    spaceNeeded = len(str(size * size))
    for x in range(spaceNeeded):
        spaces.append(" ")
        dashes.append("-")
    spaces = "".join(spaces)
    dashes = "".join(dashes)
    if not os.path.exists(file):
        with open(file, 'w') as F:
            F.close()
    else:
        with open(file, 'w') as F:
            F.write("")

    with open(file, 'a') as F:
        for y in range(size):
            for z in range(2):
                F.write("\n")
                for x in range(size):
                    if z == 0:
                        # print(f"x: {x}")
                        # print(f"y: {y}")
                        # print(f"both: {x + (y * size)}")

                        F.write(f"{genSpaces(spaceNeeded, len(str(numbers[comKeys(x, y)])))}{numbers[comKeys(x, y)]}|")
                    if z == 1 and y != (size - 1):
                        F.write(f"{dashes}-")


def genNumbers(size):
    numbersList = {}
    x = 0
    y = 0
    num = 1
    
    # start
    x = int(((size / 2) + 1) - 1)
    numbersList[comKeys(x, y)] = num

    x += 1
    y = size - 1
    num += 1
    # print(f"num: {num}")
    numbersList[comKeys(x, y)] = num

    maxIterations = size * size
    its = 0

    while len(numbersList) < (size * size - 1) and its < maxIterations:
        its += 1

        output = 0
        upRight = True
        # pdb.set_trace()
        while upRight:
            # pdb.set_trace()
            upRight = not comKeys(x + 1, y - 1) in numbersList
            if x + 1 > size - 1 or y - 1 > size - 1 or y - 1 < 0:
                if x + 1 > size - 1 and y - 1 < 0:
                    upRight = False
                    output = 2 # also false out of square but this time move down
                    y += 1
                    num += 1
                    # print(f"num: {num}")
                    numbersList[comKeys(x, y)] = num
                if y - 1 < 0:
                    upRight = False
                    output = 2 # also false out of square but this time move down
                    x += 1
                    y = size - 1
                    num += 1
                    # print(f"num: {num}")
                    numbersList[comKeys(x, y)] = num
                elif x + 1 > size - 1:
                    upRight = False
                    output = 2 # false out of square
                    x = 0
                    y -= 1
                    num += 1
                    # print(f"num: {num}")
                    numbersList[comKeys(x, y)] = num
            if upRight and output == 0:
                # can move up and right
                x += 1
                y -= 1
                num += 1
                # print(f"num: {num}")
                numbersList[comKeys(x, y)] = num

        if upRight == False and output == 0:
            # up right is taken by a number
            y += 1
            num += 1
            # print(f"num: {num}")
            numbersList[comKeys(x, y)] = num

        if num == -1 + (size * size):
            y = size - 1
            x = int(((size / 2) + 1) - 1)
            num += 1
            # print(f"num: {num}")
            numbersList[comKeys(x, y)] = num

    # print(f"numbersList {numbersList}")
    return numbersList


def main():
    if len(sys.argv) > 1:
        size = sys.argv[1]
    else:
        quit("Please input a side length")
    size = int(size)
    filename = f"squares/{size * size}.txt"
    numbers = genNumbers(size)
    genSquare(size, numbers, filename)
    print(f"generated magic square size: {size * size}")


if __name__ == "__main__":
    if not os.path.exists("squares"):
        os.mkdir("squares")
    main()
