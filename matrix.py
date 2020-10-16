#!/usr/bin/python3

from data import matrix1, matrix2

m1Size = len(matrix1)
m2Size = len(matrix2)

# Addition of matrixes


def add():

    result = []

    if m1Size == m2Size:
        for x in range(m1Size):
            newRow = []

            for y in range(len(matrix1[x])):
                newRow.append(matrix1[x][y] + matrix2[x][y])
            result.append(newRow)
    else:
        print('Matrix size must be same for addition')

    printFormatted(result)

# Substraction of matrixes


def minus():

    result = []

    if m1Size == m2Size:
        for x in range(m1Size):
            newRow = []

            for y in range(len(matrix1[x])):
                newRow.append(matrix1[x][y] - matrix2[x][y])
            result.append(newRow)
    else:
        print('Matrix size must be same for substraction')

    printFormatted(result)

# Generate matrixes


def generateResultMatrix():
    result = []
    for _ in range(len(matrix1)):
        newRow = []
        for _ in range(len(matrix2)):
            newRow.append(0)
        result.append(newRow)
    return result


def multiply():
    result = generateResultMatrix()

    for x in range(len(matrix1)):
        for y in range(len(matrix2[0])):
            for z in range(len(matrix2)):
                result[x][y] += matrix1[x][z] * matrix2[z][y]

    printFormatted(result)

# Formatted print function


def printFormatted(result):
    for x in range(len(result)):
        for y in range(len(result[x])):
            if result[x][y] == result[x][0] and y == 0:
                print('|' + str(result[x][y]), end=' , ')
                continue
            if result[x][y] == result[x][len(result[x]) - 1] and y == (len(result[x]) - 1):
                print(str(result[x][y]) + '|', end='')
                continue
            print(result[x][y], end=' , ')
        print()


# Transpose matrix

def transopse(matrix):
    result = []

    for _ in range(len(matrix)):
        newRow = []
        for _ in range(len(matrix1[0])):
            newRow.append(0)

        result.append(newRow)

    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            result[y][x] = matrix[x][y]

    printFormatted(result)


# Main execution point

def transposeUI():
    print("Choose which matrix , 1 or 2")

    try:
        ans = int(input(">> "))

        if ans == 0:
            consoleUI()
        elif ans == 1:
            transopse(matrix1)
        elif ans == 2:
            transopse(matrix2)
        else:
            print("Invalid option :/")
            transposeUI()
    except:
        print("Invalid option :/")
        transposeUI()


def consoleUI():
    print("Choose an option")
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
    print("4) Transpose")
    option = input(">> ")

    try:
        parsed = int(option)

        if parsed == 1:
            print('Addition of matrixes')
            add()
            print()
        elif parsed == 2:
            print('Substraction of matrixes')
            minus()
            print()
        elif parsed == 3:
            print('Multiplication of matrixes')
            multiply()
            print()
        elif parsed == 4:
            transposeUI()
        else:
            consoleUI()
    except:
        print("Invalid option :/")
        consoleUI()


if __name__ == "__main__":
    consoleUI()
