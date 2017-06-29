def rotate_dynamic_array(array, d, n):
    d = d % n
    
    for i in range(d):
        array.append(array.pop(0))
    return array

def rotate_by_new_array(array, d, n):
    # This solution will run in O(n)
    # And the space required will be O(n), as we are creating a new array
    d = d % n
    # array = array[d:] + array[:d] # The python way
    # return array

    new_array = []  # The manual way
    for i in range(d, n):
        new_array.append(array[i])

    for i in range(0, d):
        new_array.append(array[i])

    return new_array
    
if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n, d = map(int, input().split())
        array = input().split()
        
        print(' '.join(rotate_by_new_array(array, d, n)))
