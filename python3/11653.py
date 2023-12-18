n = int(input())
op = 2

while n > 1:
    if n % op != 0:
        op +=1
        continue
    print(op)
    n = int(n/op)