T = int(input())

for _ in range(T):
    string = input()

    for letter in string[::2]:
        print(letter, end="")

    print(" ", end="")
    for letter in string[1::2]:
        print(letter, end="")

    print()
