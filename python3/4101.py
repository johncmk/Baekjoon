def is_a_bigger(a,b):
    if a==0 and b == 0:
        return ""
    return "Yes" if a > b else "No"

while True:
    a,b=map(int,input().split())
    msg=is_a_bigger(a,b)
    if(msg == ""):
        break
    print(msg)