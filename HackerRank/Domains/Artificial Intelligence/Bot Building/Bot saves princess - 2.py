#
def nextMove(n,r,c,grid):
    # Finding Princess's coordinates
    for i, row in enumerate(grid):
        if 'p' in row:
            pr, pc = i, list(row).index('p')
            break
            
    if pc < c:
        return 'LEFT'
    elif pc > c:
        return 'RIGHT'
    else:
        if pr < r:
            return 'UP'
        else:
            return 'DOWN'
    
n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))

