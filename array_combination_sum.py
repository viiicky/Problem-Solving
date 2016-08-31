def combination(numbers, total):
    '''Return all possible subset from the given collection 'numbers'
    whose sum results in 'total'.
    '''
    pair_group = []

    for index, number in enumerate(numbers):
        if number == total:
            pair_group.append([number])
            continue

        if number > total:
            continue

        pair = []
        pair.append(number)
        
        new_total = total - number
        partial_pair_group = combination(numbers[index+1:], new_total)

        for p in partial_pair_group:
            pair_group.append(pair+p)

    return pair_group

result = combination([1, 1, 1, 2, 3, 5, 7], 8)
result_set = {tuple(r) for r in result}
print(result_set)
