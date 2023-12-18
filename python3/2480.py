def reward(a,b,c):
    max_n=max(a,b,c)
    min_n=min(a,b,c)
    mid_n=(a+b+c)-max_n-min_n

    if (mid_n == max_n and mid_n == min_n) and max_n == min_n:
        return 10000 + (mid_n * 1000)
    if (mid_n == max_n or mid_n == min_n) and max_n != min_n:
        return 1000 + (mid_n * 100)
    return max_n * 100

a,b,c=map(int,input().split())
print(reward(a,b,c))