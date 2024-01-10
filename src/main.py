import os
import math
import pdb

def genEmptySquare(size, numbers, file):
    if len(numbers) != size * size:
        quit("list is the wrong size")
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
                        print(f"x: {x}")
                        print(f"y: {y}")
                        print(f"both: {x + (y * size)}")
                        F.write(f"{numbers[x, y]}|")
                    if z == 1 and y != (size - 1):
                        F.write("--")


def genNumbers(size):
    list = {}
    x = 0
    y = 0
    num = 1
    
    # start
    x = int(((size / size) + 1))
    list[x, y] = num

    x += 1
    y = size
    num += 1
    print(f"num: {num}")
    list[x, y] = num

    maxIterations = size * size
    its = 0

    while len(list) < (size * size - 1) and its < maxIterations:
        its += 1

        output = 0
        upRight = True
        # pdb.set_trace()
        while upRight:
            upRight = all(k in list for k in [(x + 1), (y - 1)])
            if x + 1 > size or y - 1 > size:
                upRight = False
                output = 2 # false out of square
            if upRight == True:
                x += 1
                y -= 1
                num += 1
                print(f"num: {num}")
                list[x, y] = num

        if output == 2:
            x = 0
            y -= 1
            num += 1
            print(f"num: {num}")
            list[x, y] = num
        elif output == 0:
            y += 1
            num += 1
            print(f"num: {num}")
            list[x, y] = num

        if num == -1 + (size * size):
            y = size
            x = int(((size / size) + 1))
            num += 1
            print(f"num: {num}")
            list[x, y] = num

    print(f"list {list}")
    return list


    # fill to the square
    with open(file, 'r') as F:
        content = F.read().splitlines()
        for x in range(len(content)):
            rows = content[x]
            if not "|" in rows:
                continue

            # 2 chars per col
            for y in range(len(rows)):
                char = rows[y]
                if char == " ":
                    content[x][y] = str(list[x * (y + 1)])
                print(f"char: {char}")


def main():
    print("welcome to main")
    numbers = genNumbers(3)
    genEmptySquare(3, numbers, "9.txt")


if __name__ == "__main__":
    main()
