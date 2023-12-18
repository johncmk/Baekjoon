t = int(input())

for i in range(t):
    r,str = input().split()
    r = int(r)
    output=""
    for el in str:
        output += (r*el)
    print(output)