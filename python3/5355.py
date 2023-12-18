t = int(input())

ans=0
for i in range(t):
    eq = input().split(' ')
    ans = float(eq[0])
    for el in eq[1:]:
        if el == '@':
            ans *= 3
        elif el == '%':
            ans += 5
        elif el == '#':
            ans -= 7
        else:
            continue
    print(format(ans,'.2f'))