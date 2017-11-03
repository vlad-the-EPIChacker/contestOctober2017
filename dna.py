f = open("/Volumes/PSCSTA/JudgeFiles/dna.txt")
file = f.readlines()
nfile = int(file[0])

valid = True

for i in range(1,2*nfile+1,2):
    valid=True
    line = file[i].strip()
    line2 = file[i+1].strip()

    for ii in range(0,10,1):
        if line[ii] == 'G' and line2[ii] != 'C':
            valid = False
            break
        if line[ii] == 'T' and line2[ii] != 'A':

            valid = False
            break
        if line[ii] == 'C' and line2[ii] != 'G':

            valid = False
            break

        if line[ii] == 'A' and line2[ii] != 'T':

            valid = False
            break

    if valid:
        print('Valid')
    else:
        print('Invalid')
