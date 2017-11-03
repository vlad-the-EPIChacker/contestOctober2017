
def swap(r,t,y):
    u=r[t]
    r[t]=r[y]
    r[y]=u

def scramble(c,k,glob):
    if k>=len(c)-1:
        glob.append([i for i in c])
        return
    for i in range(k,len(c)):
        swap(c,k,i)
        scramble(c,k+1,glob)
        swap(c, k, i)
    return

f = open("zipcode.txt")
file = f.readlines()
nfile = int(file[0])

for i in range(1,nfile+1,1):
    glob=[]
    line = file[i].strip().split()
    final=[]
    c=[j for j in list(line[0])]
    f=[j for j in list(line[1])]
    difs=[]
    scramble(c,0,glob)
    for j in glob:
        difs.append(abs(int(''.join(j))-int(''.join(f))))
    difs=sorted(difs)
    print ''.join(glob[difs.index(min(difs))]), min(difs)
