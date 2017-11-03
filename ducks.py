f = open("/Volumes/PSCSTA/JudgeFiles/ducks.txt")
file = f.readlines()
nfile = int(file[0])
r=[31,28,31,30,31,30,31,31,30,31,30,31]

for i in range(1,nfile+1,1):
    line = file[i].strip().split()
    d = int(line[0])
    month = int(line[1].split("/")[0])
    day = int(line[1].split("/")[1])
    day += sum(r[:month-1])
    for ii in range(0, day,1):
        if ii%10==0 and ii>0:
            d *= 2
        if ii%24==0 and ii>0:
            d *= 0.75
    print int(d)

