def conversion(n,b):
    n1=[]
    while n>0:
        n1.append(n % b)
        n = n/b
    return n1

f = open("palindrome2.txt")
file = f.readlines()
nfile = int(file[0])

for i in range(1,nfile+1,1):
    line = int(file[i].strip())
    b1=[]
    for ii in range(2, 21):
        n=conversion(line,ii)
        if n == list(reversed(n)):
            b1.append(str(ii))
    if len(b1)==0:
        print 'None'
    else:
        print ', '.join(b1)
