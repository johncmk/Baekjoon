size = 5
total = 0
for i in range(size):
    el = int(input())
    total += 40 if el < 40 else el
print(int(total/size))