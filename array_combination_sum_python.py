'''Return all possible subset from the given collection 'numbers'
    whose sum results in 'total'.
'''

from itertools import combinations

numbers = [1, 1, 1, 2, 3, 5, 7]
total = 8

required_combination = set()
for i in range(1, len(numbers)+1):
    combination_list = list((combinations(numbers, i)))
    
    for comb in combination_list:
        if sum(comb) == total:
            required_combination.add(comb)

print(required_combination)
