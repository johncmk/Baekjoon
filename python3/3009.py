def set_dic(d,k):
    d[k] = 1 if k not in d else d[k]+1

def get_single_li(d):
    return [k for k,v in d.items() if v == 1]

x={}
y={}
for _ in range(3):
    a,b=map(int,input().split())
    set_dic(x,a)
    set_dic(y,b)

li_x=get_single_li(x)
li_y=get_single_li(y)

print("%s %s"%(li_x[0],li_y[0]))