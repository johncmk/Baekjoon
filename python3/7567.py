a = input()
ret=0
for i in range(1, len(a)):
    ret = ret+5 if a[i-1] == a[i] else ret+10
print(ret+10)