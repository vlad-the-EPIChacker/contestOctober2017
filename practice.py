f = open("practice.txt")
file = f.readlines()

for i in range(1,int(file[0])+1,1):
    line = file[i].strip()
    bool=True
    for ii in range(len(line)):
        if line[ii] != "A" and line[ii] != "B" and line[ii] != "C":
            print line[ii]
            bool=False
            break
    if bool:
        print None