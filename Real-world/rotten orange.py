l=[[2,1,0,2,1],[1,0,1,2,1],[1,0,0,2,1]]
days = 0
while True:
    l1 = [[j for j in i] for i in l]
    c,good=0,0
    row,col=len(l),len(l[0])
    for i in range(row):
        for j in range(col):
            if l[i][j] == 0:
                continue
            elif l[i][j]==1:
                    good+=1
            else:
                if (i - 1) >= 0 and l[i - 1][j] == 1:
                    c +=1
                    l1[i - 1][j] = 2
                if (i + 1) < row and l[i + 1][j] == 1:
                    c += 1
                    l1[i + 1][j] = 2
                if (j - 1) >= 0 and l[i][j - 1] == 1:
                    c += 1
                    l1[i][j - 1] = 2
                if (j + 1) < col and l[i][j + 1] == 1:
                    c += 1
                    l1[i][j + 1] = 2
    if c>0:
        l = l1
        days+=1
    else:
        print(-1 if c==0 and good>0 else days)
        break

