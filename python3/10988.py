def is_p(txt):
    pt_a=0
    pt_b=len(txt)-1

    while (pt_a - pt_b) < 0:
        a=txt[pt_a]
        b=txt[pt_b]

        if a != b:
            return False
        
        pt_a+=1
        pt_b-=1

    return True

txt=input()
print(int(is_p(txt)))