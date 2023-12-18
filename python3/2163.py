n,m=map(int,input().split())

ch_size=n * m
ch_split_num=0

while ch_size > 1:
    ch_split_num+=1
    ch_size-=1

print(ch_split_num)