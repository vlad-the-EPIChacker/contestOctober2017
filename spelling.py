f = open("/Volumes/PSCSTA/JudgeFiles/spelling.txt")
file = f.readlines()
nfile = int(file[0])

for i in range(1,nfile+1,1):
    line = file[i].strip().split()
    word=list(line[0])
    letters=line[2:]
    for ii in letters:
        if ii in word:
            word.remove(ii)
    if len(word)==0:
        print 'yes'
    else:
        print 'no'