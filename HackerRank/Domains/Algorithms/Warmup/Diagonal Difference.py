N = int(input())

sum = 0
for i in range(N):
    row = [int(x) for x in input().split()]
    sum += row[i] - row[-i-1]
    
print (abs(sum))
