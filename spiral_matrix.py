#!/usr/bin/env python3
# To traverse a matrix spirally
# Fond this on glassdoor:
# https://www.glassdoor.co.in/Interview/To-traverse-a-matrix-spirally-QTN_1044131.htm

def traverseMatrixSpirally(A):
    '''Print matrix elements in spiral order.'''

    # set margins
    topRow = 0
    rightCol = len(A[0]) - 1
    bottomRow = len(A) - 1
    leftCol = 0

    # calculate dimensions
    length = len(A[0])
    breadth = len(A)

    while True:
        if topRow > bottomRow or leftCol > rightCol:    # if margins crossed each other, it means the matrix has been fully traversed already
            return
        else:
            # print row from left to right
            print(A[topRow][leftCol : rightCol + 1])
            topRow += 1

        if topRow > bottomRow or leftCol > rightCol:
            return
        else:
            col = [row[rightCol] for row in A]
            # print col from up to down
            print(col[topRow : bottomRow + 1])
            rightCol -= 1

        if topRow > bottomRow or leftCol > rightCol:
            return
        else:
            # print row from right to left
            print(list(reversed(A[bottomRow]))[(length-rightCol) - 1 : length - leftCol])
            bottomRow -= 1

        if topRow > bottomRow or leftCol > rightCol:
            return
        else:
            col = [row[leftCol] for row in A]
            # print col from down to up
            print(list(reversed(col))[(breadth-bottomRow) - 1 : breadth - topRow])
            leftCol += 1

if __name__ == '__main__':

    A = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 10, 11, 12],
         [13, 14, 15, 16]]

    A = [[1, 2, 3, 4, 5],
         [6, 7, 8, 9, 10],
         [11, 12, 13, 14, 15],
         [16, 17, 18, 19, 20],
         [21, 22, 23, 24, 25]]
    
    A = [[1, 2, 3, 4, 5, 6,],
         [7, 8, 9, 10, 11, 12],
         [13, 14, 15, 16, 17, 18]]
    
    A = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
         [10, 11, 12],
         [13, 14, 15],
         [16, 17, 18]]

    traverseMatrixSpirally(A)
