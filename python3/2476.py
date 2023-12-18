t=int(input())

reward=0
final_reward=0
for _ in range(t):
    a,b,c=map(int,input().split())
    
    sum_n=a+b+c
    max_n=max(a,b,c)
    min_n=min(a,b,c)
    mid_n=sum_n-max_n-min_n

    if mid_n == max_n and mid_n == min_n:
        reward=10000+(mid_n*1000)
    elif mid_n == max_n or mid_n == min_n and max_n != min_n:
        reward=1000+(mid_n*100)
    else:
        reward=max_n*100

    if reward > final_reward:
        final_reward=reward

print(final_reward)