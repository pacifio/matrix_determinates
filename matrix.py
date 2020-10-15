#!/usr/bin/python3

"""
Copyright 2020> Adib Mohsin

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

matrix1 = [
    [4, 8, 4],
    [0, 4, 4],
    [8, 0, 8]
]

matrix2 = [
    [2, -4, -2],
    [2, 0, -1],
    [-2, 4, 1]
]

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

# Main execution point


def consoleUI():
    print("Choose an option")
    print("1) Add")
    print("2) Subtract")
    print("3) Multiply")
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
        else:
            consoleUI()
    except:
        print("Invalid option :/")
        consoleUI()


if __name__ == "__main__":
    consoleUI()
