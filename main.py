ab = input()
a = int(ab.split()[0])
b = int(ab.split()[1])
x = 0
v = False
while a!=b:
    if a>b:
        try:
            x += a // b
            a = a % b
        except ZeroDivisionError:
            break
    elif b>a:
        try:
            x += b // a
            b = b % a
        except ZeroDivisionError:
            break



if x != 0:
    x-=1
print(x)