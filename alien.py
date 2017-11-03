f=open("/Volumes/PSCSTA/JudgeFiles/alien.txt")
file=f.readlines()
nfile=int(file[0])
l=1
c=0

while c<nfile:
    nlines=[int(i) for i in file[l].split()]
    code=[]
    for i in range(l+1,nlines[0]+l+1):
        code.append([int(ii) for ii in file[i].strip().split()])

    for i in range(0,len(code)):
        for ii in range(0,len(code[0])):
            code[i][ii]=code[i][ii]/7


    for i in range(0,len(code),2):
        for ii in range(0,len(code[0])):
            code[i][ii]=code[i][ii]-19

    for i in range(0,len(code)):
        for ii in range(0,len(code[0])):
            code[i][ii]=chr(code[i][ii])
    s=''
    for ii in range(0,len(code[0])):
        for i in range(0,len(code)):
            s += code[i][ii]
    print s
    l+=nlines[0]+1
    c+=1