t = int(input())

msg = ""

for _ in range(t):
    r,e,c = map(int, input().split())

    ad_r = e-c

    if ad_r > r:
        msg = "advertise"
    elif ad_r < r:
        msg = "do not advertise"
    else:
        msg = "does not matter"

    print(msg)