final=[]
def swap(r,x1,x2):
    temp=r[x2]
    r[x2]=r[x1]
    r[x1]=temp
    return r

def permute1(s,p):
    global final
    s1=s
    if len(s)-p==0:
        final.append(s)
        return
    for i in range(p,len(s)):
        s1=''.join(swap(list(s1),i,p))
        permute1(s1,p+1)
        s1 = ''.join(swap(list(s1), i, p))

def permute(s,p):
    final=[]
    permute1(s,p)

permute1('abc',0)
print final,len(final)

