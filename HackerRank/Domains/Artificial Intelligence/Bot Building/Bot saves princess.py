#!/usr/bin/python
# It takes O(n) time
def displayPathtoPrincess(n,grid):
    steps = int((n-1) / 2)
    if 'p' == grid[0][0] or 'p' == grid[0][n-1]:
        for _ in range(steps):
            print('UP')
        if 'p' == grid[0][0]:
            for _ in range(steps):
                print('LEFT')
        else:
            for _ in range(steps):
                print('RIGHT')
    else:
        for _ in range(steps):
            print('DOWN')
        if 'p' == grid[n-1][0]:
            for _ in range(steps):
                print('LEFT')
        else:
            for _ in range(steps):
                print('RIGHT')
                
#print all the moves here
m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)

