def ransom_note(magazine, ransom):
    magazine_hash = {}
    for word in magazine:
        magazine_hash[word] = magazine_hash.get(word, 0) + 1
        
    ransom_hash = {}
    for word in ransom:
        ransom_hash[word] = ransom_hash.get(word, 0) + 1
        
    for key, value in ransom_hash.items():
        if (not magazine_hash.get(key)) or magazine_hash[key] < value:
            return False
    return True
    

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    

