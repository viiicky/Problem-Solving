# Write a program to reverse an array or string
# We are given an array (or string), the task is to reverse the array.

def reverse_array(array):
    # This approach will run in O(n) time, but it will create a new array,
    # that means it requires an auxilliary space of O(n).'''
    new_array = []

    for item in array[::-1]:
        new_array.append(item)

    return new_array

def swap(array, start, end):
    temp = array[start]
    array[start] = array[end]
    array[end] = temp

def reverse_array_in_place(array):
    # This approach will run in O(n) time, but it will reverse the array in place.
    # This will require a constant space of swap variable. O(1)'''
    start = 0;
    end = len(array) - 1

    '''
    while end - start > 0:  # calculating after each iteration whether we reached the middle
        swap(array, start, end)
        start += 1
        end -= 1
    ''' 

    for _ in range(len(array)//2):  # calculating mathematically the number of iterations in advance and providing it
        swap(array, start, end)     # i.e. after each iteration we we just do a comparison, while in the above appraoch,
        start += 1                  # while in the above commented approach, after each iteration we need to perform one arithmetic operation + one comparison
        end -= 1

    return array

def reverse_array_recursive(array, start, end):
    if end - start <= 0:
        return array

    swap(array, start, end)
    return reverse_array_recursive(array, start+1, end-1)

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        input()
        array = input().split()
        print(' '.join(reverse_array_in_place(array)))
        # print(' '.join(reverse_array_recursive(array, 0, len(array)-1)))
        
