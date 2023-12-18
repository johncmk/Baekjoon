t=int(input())
d={0:0,1:0}

for _ in range(t):
    el=int(input())
    d[el]+=1

a=d[0]
b=d[1]

msg = ""
if a < b:
    msg="Junhee is cute!"
else:
    msg="Junhee is not cute!"

print(msg)
