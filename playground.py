f = open("playground.txt")
file = f.readlines()
nfile = int(file[0])

for i in range(1,nfile+1,1):
    line = file[i].split()

    price = float(line[0])
    budget = float(line[1])

    print int(round((budget/price/4.0)**2,0))
