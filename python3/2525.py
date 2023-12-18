h,m = map(int, input().split())
cook_m = int(input())

new_m = m + cook_m
m = new_m % 60

if new_m >= 60:
    h = h + new_m // 60 # or h = h + int(new_m / 60)
h = h % 24

print("%s %s"%(h,m))