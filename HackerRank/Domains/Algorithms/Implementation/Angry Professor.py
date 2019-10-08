T = int(input())
for _ in range(T):
    N, K = [int(x) for x in input().split()]
    a = [x for x in input().split() if int(x) <= 0]
    print('NO') if len(a) >= K else print('YES')
