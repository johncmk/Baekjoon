def ans(k,m,n):
    r = (k*m) - n
    return 0 if r <= 0 else r

k,m,n=map(int,input().split())
print(ans(k,m,n))