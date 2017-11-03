f = open("/Volumes/PSCSTA/JudgeFiles/magic.txt")
file = f.readlines()
nfile = int(file[0])

for i in range(1,3*nfile+1,3):
    n=0
    rows = [file[i+ii].strip().split() for ii in range(0,3)]
    cols = [[rows[iii][ii] for iii in range(0,3)] for ii in range(0,3)]
    diagnols = [[rows[0][0],rows[1][1],rows[2][2]],[rows[0][2],rows[1][1],rows[2][0]]]
    for ii in rows:
        if sum([int(iii) for iii in ii])!=15:
            n += 1
    for ii in cols:
        if sum([int(iii) for iii in ii])!=15:
            n += 1
    for ii in diagnols:
        if sum([int(iii) for iii in ii])!=15:
            n += 1
    print n