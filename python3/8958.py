'''
def add_ret(ret,n):
    for i in range(1,n+1):
        ret+=i
    return ret

def get_ret(s):
    ret = 0
    d={"O":0,"X":0}

    for el in s:
        if el == "X":
            if d["O"] == 0:
                continue
            ret = add_ret(ret,d["O"])
            d={"O":0,"X":0}
        else:
            d["O"] += 1

    return add_ret(ret,d["O"])

n = int(input())
for _ in range(n):
    s = input()
    ret = get_ret(s)
    print(ret)
'''

'''
n=int(input())
for i in range(0,n):
    count,c=0,1
    s=list(input())
    for j in s:
        if j=='O':
            count+=c
            c+=1
        else:
            c=1
    print(count)
'''

'''
n = int(input())

for _ in range(n):
    ox_list = list(input())
    score = 0  
    sum_score = 0  # 새로운 ox리스트를 입력 받으면 점수 합계를 리셋한다.
    for ox in ox_list:
        if ox == 'O':
            score += 1  # 'O'가 연속되면 점수가 1점씩 커진다.
            sum_score += score  # sum_score = sum_score + score
        else:
            score = 0
    print(sum_score)
'''

n = int(input())
for _ in range(n):
    num = 0
    total_num = 0
    s = input()
    for el in s:
        if el == "O":
            num += 1
            total_num += num
        else:
            num = 0
    print(total_num)