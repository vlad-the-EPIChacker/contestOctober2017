def AddBook(l,n,s):
    l=[i for i in l]
    l1=l
    if l1[s]-n>-1:
        l1[s] -= n
    return l1

def Check(l,n):
    l1=[i for i in l]
    for i in range(0,len(l1)):
        if l1[i]-n>-1:
            return True
    return False

def bookshelf(b,l):
    l=[i for i in l]
    final=[]
    end=True
    for i in b:
        if Check(l,i):
            end=False
            break
    if end:
        return b
    for i in range(0,len(b)):
        for u in range(0,len(l)):
            print(i,u)
            if l[u]>b[i]-1:
                final.append(bookshelf([b[ii] for ii in range(0,len(b)) if ii!=i],AddBook(l,b[i],u)))
    lens=[len(i) for i in final]
    return final[lens.index(min(lens))]

f = open("bookshelf1.txt")
file = f.readlines()
nfile = int(file[0])

for i in range(1,3*nfile+1,3):
    shelfs = [int(ii) for ii in file[i].strip().split()]
    left = bookshelf([int(ii) for ii in file[i+2].strip().split()],[shelfs[1] for ii in range(0,shelfs[0])])
    print left