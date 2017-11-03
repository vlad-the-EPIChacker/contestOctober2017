f = open("/Volumes/PSCSTA/JudgeFiles/sorting.txt")
file = [int(i) for i in f.readlines()]
nfile = int(file[0])
file=file[1:]
file=reversed(sorted(file))
for i in file:
    print i