# Majority Element: A majority element in an array A[] of size n is an element that appears more than n/2 times (and hence there is at most one such element).
# Write a program which takes an array and emits the majority element (if it exists), otherwise prints NONE as follows:
# For I/P : 3 3 4 2 4 4 2 4 4
# O/P : 4 

# For I/P : 3 3 4 2 4 4 2 4
# O/P : NONE
# Problem Link: http://www.geeksforgeeks.org/majority-element/

T = int(input())
for _ in range(T):
    N = input()
    A = [int(n) for n in input().split()]
    
    hash_table = {}
    
    # iterate list and count each occurence
    for number in A:
        hash_table[number] = hash_table.get(number, 0) + 1
        # if the count becomes more than half size
        # then the number is majority number
        if hash_table[number] > N/2:
            print(number)
            break
    else:
        print("NO Majority Element")