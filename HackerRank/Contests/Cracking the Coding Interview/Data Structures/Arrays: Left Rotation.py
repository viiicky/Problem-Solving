def array_left_rotation(a, n, k):
    k = k % n
    
    return a[k:]+a[0:k]
    

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')

