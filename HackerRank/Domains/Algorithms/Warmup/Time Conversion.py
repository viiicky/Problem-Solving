time = input()

hh = int(time[0]) * 10 + int(time[1])

if time[8] == 'P':
    if hh != 12:
        hh += 12
else:
    if hh == 12:
        hh = 0
        
if hh < 10:
    print(0, end='')
print(hh,end='')
print(time[2:-2])
