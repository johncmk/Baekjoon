s = int(input())

ret = 0
i = 1

while True:
    if ret > s:
        break
    ret += i
    i += 1
print(i-2)