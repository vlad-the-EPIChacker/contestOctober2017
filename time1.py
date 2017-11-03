f = open("/Volumes/PSCSTA/JudgeFiles/time.txt")
file = f.readlines()
nfile = int(file[0])

for i in range(1,nfile+1,1):
    n = int(file[i])

    days = 0
    hrs = 0
    min = 0
    sec = 0

    days = n/(60**2*24)
    n -= days * 60**2*24

    hrs = n / (60 ** 2)
    n -= hrs * 60 ** 2

    min = n / (60)
    n -= min * 60

    sec = n





    print days,"days",hrs,"hrs",min,"min",sec,"sec"
