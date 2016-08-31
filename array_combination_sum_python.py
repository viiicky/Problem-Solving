from itertools import combinations

numbers = [1, 1, 1, 2, 3, 5, 7]
total = 8

required_combination = []
for i in range(1, len(numbers)+1):
    combination_list = list((combinations(numbers, i)))
    
    for comb in combination_list:
        if sum(comb) == total:
            required_combination.append(comb)

print(set(required_combination))
