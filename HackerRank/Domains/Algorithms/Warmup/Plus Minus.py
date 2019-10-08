N = int(input())
A = [float(_) for _ in input().split()]

zero = neg = pos = 0
for x in A:
    if not x:
        zero += 1
    elif x < 0:
        neg += 1
    else:
        pos += 1
        
print(("%.3f\n%.3f\n%.3f") %(pos/N, neg/N, zero/N))
