h,m,s = map(int, input().split())
cook_s = int(input())

new_s = s + cook_s

if new_s >= 60:
    m = m + int(new_s/60)
if m >= 60:
    h = h + int(m/60)
h = h % 24
m = m % 60
s = new_s % 60

print("%s %s %s"%(h,m,s))