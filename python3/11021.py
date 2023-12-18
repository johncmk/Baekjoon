cases = int(input())

for i in range(cases):
    n1,n2=map(int, input().split())
    ans=n1 + n2
    print("Case #%s: %s"%(i+1,ans))