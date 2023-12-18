n = int(input())

is_yun = (n % 4 == 0 and n % 100 != 0) or n % 400 == 0
print( 1 if is_yun else 0)