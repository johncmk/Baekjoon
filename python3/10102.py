t = int(input())
c = input()

d={"A":0, "B":0}

for el in c:
    d[el]+=1

total_a=d["A"]
total_b=d["B"]
msg=""

if total_a > total_b:
    msg = "A"
elif total_a < total_b:
    msg = "B"
else:
    msg = "Tie"

print(msg)