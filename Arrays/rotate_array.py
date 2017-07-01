# Program for array rotation
# Write a function that rotates array of size n by d elements
# Prolem Link: http://www.geeksforgeeks.org/array-rotation/
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

def rotate_in_place(array, d, n):
    # This solution will run in O(n)
    # And the space required will be O(d%n)
    d = d % n

    # put the first d elements in a queue
    queue = []
    for i in range(d):
        queue.append(array[i])

    # shift elements after dth position from right to left
    for i in range(n-d):
        array[i] = array[i+d]

    # moev left over elemets from the queue at the end place of the array
    for i in range(n-d, n):
        array[i] = queue.pop(0)

    del(queue)

    return array
    
if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n, d = map(int, input().split())
        array = input().split()

        print(' '.join(rotate_in_place(array, d, n)))
