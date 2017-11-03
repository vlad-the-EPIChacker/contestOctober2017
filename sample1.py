f=open("sample.txt")
file=f.readlines()
nfile=int(file[0])
l=1
c=0
while c<nfile:
    nlines=int(file[l].split())
    l+=nlines+1
    c+=1