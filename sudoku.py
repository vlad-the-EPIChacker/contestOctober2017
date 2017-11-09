def PrintBoard(b):
    for i in b:
        print ' '.join(i)

def FindMissing(b):
    final=[]
    for i in range(0,len(b)):
        for ii in range(0,len(b[i])):
            if b[i][ii]=='?':
                final.append((ii,i))
    return final

def Valid():
    for i in range(0,3):
        for ii in range(0,3):
            check=[]
            x1=3*ii
            y1=3*i
            for y in range(y1,y1+3):
                for x in range(x1, x1 + 3):
                    if board[y][x] not in check or board[y][x]=='?':
                        check.append(board[y][x])
                    else:
                        return False
    return True

def Valid1(x,y):
    row=[]
    for i in board[y]:
        if i not in row:
            row.append(i)
    if len(row)<9:
        return False
    col=[]
    for i in [i[x] for i in board]:
        if i not in col:
            col.append(i)
    if len(col)<9:
        return False
    return True

def Solve(m):
    if m>=len(missing):
        if Valid():
            PrintBoard(board)
            return True
        else:
            return False
    for i in range(1,10):
        x = missing[m][0]
        y = missing[m][1]
        board[y][x]=str(i)
        if Valid1(x,y):
            if Solve(m+1):
                solution.append(i)
                return True
        board[y][x]='?'

f=open("sudoku.txt")
file=f.readlines()
board=[i.strip().split() for i in file[1:]]
missing=FindMissing(board)
solution=[]
Solve(0)
solution=[i for i in reversed(solution)]
print solution