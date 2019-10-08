AD, AM, AY = map(int, input().split())
ED, EM, EY = map(int, input().split())

if AY != EY:
    if AY < EY:
        print(0)
        exit()
    print(10000)
elif AM != EM:
    if AM < EM:
        print(0)
        exit()
    print(500*(AM-EM))
else:
    if AD <= ED:
        print(0)
        exit()
    print(15*(AD-ED))
