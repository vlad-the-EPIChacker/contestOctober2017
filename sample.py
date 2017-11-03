f = open("practice.txt")
file = f.readlines()
nfile = int(file[0])

for i in range(1,nfile+1,1):
    line = file[i].strip()
