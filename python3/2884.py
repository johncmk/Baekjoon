h,m=map(int,input().split())
ch_m=45

if m < 45:
    m = m + 60 - 45
    h=23 if h == 0 else h-1
else:
    m = m-45

print("%s %s"%(h, m))