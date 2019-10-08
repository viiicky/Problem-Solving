def number_needed(a, b):
    string1_dict = {}
    string2_dict = {}
    
    for character in a:
        string1_dict[character] = string1_dict.get(character, 0) + 1;
        
    for character in b:
        string2_dict[character] = string2_dict.get(character, 0) + 1;

    count = 0
    for key, value in string1_dict.items():
        value2 = string2_dict.get(key)
        if value2:
            count += abs(value - value2)
        else:
            count += value
            
    for key, value in string2_dict.items():
        value1 = string1_dict.get(key)
        if not value1:
            count += value
            
    return count
        
    
        

a = input().strip()
b = input().strip()

print(number_needed(a, b))

