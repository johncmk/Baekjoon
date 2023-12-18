n1,n2,n3 = map(int, input().split())

sum_n = n1+n2+n3
max_n = max(n1,n2,n3)
min_n = min(n1,n2,n3)

print(sum_n-max_n-min_n)