import fileinput

N = int(input())

phoneBook = {}
for _ in range(N):
    name, phoneNumber = input().split()
    phoneBook[name] = phoneNumber
    
for line in fileinput.input():
    name = line.strip()
    if name not in phoneBook:
        print("Not found")
    else:
        print(name, "=", phoneBook[name], sep="")
