# def _min(a,b):
#     return a if a < b else b

# def lcm(n1,n2):
#     ret = (n1 * n2)
#     for i in range(_min(n1,n2),ret):
#         if i % n1 == 0 and i % n2 == 0:
#             ret = _min(ret,i)
#             break
#     return ret

# def lcm(n1,n2):
#     ret = (n1 * n2)
#     i = _min(n1,n2)
#     while not (i % n1 == 0 and i % n2 == 0):
#         ret = _min(ret,i)
#         i+=1
#     return ret

# def lcm2(a,b):
#     print("### lcm2 ###")
#     result = a * b

#     while True:
#         if b == 0:
#            break
#         a = b
#         b = a % b

#     return int(result/a)

# def gcd(x, y):  #최대공약수 구하기
#   print("### gcd ###")
#   if y == 0:
#     print("x : ",x)
#     return x
#   else:
#     gcd_loop = gcd(y, x%y)
#     print("gcd_loop : ",gcd_loop)
#     return gcd_loop
  
# def gcd_loop(a,b):
#    while True:
#       if b == 0:
#          return a
#       a = b
#       b = a % b


# def lcm3(x, y):  ## 최소공배수 구하기
#   print("### lcm3 ###")
#   result = (x*y) // Euclidean(x,y)
#   print("result : ",result)
#   return result

# def Euclidean(a, b):
#     print("### Euclidean ###")

#     print("a : ", a)
#     print("b : ", b)

#     while b != 0:
#         r = a % b
#         print("r = %s %s %s = %s"%(a,'%',b,r))
#         a = b
#         print("a = b : ",a)
#         b = r
#         print("b = r : ",b)

#     print("final a : %s"%(a))
#     return a


def gcd(a,b):
    while b > 0:
        r = a % b
        a = b
        b = r
    return a

def lcm(a,b):
    return int((a*b)/gcd(a,b))

t = int(input())
for i in range (t):
    n1,n2=map(int, input().split())
    print(lcm(n1,n2))
