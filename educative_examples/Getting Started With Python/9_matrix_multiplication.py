a = [ [1,2,3,4] , [5,6,7,8] , [9,10,11,12] ]  
b = [ [10,20] , [30,40] , [50,60] , [70,80] ]

aROWS, aCOLS = len(a), len(a[0])
bROWS, bCOLS = len(b), len(b[0])
cROWS, cCOLS = aROWS, bCOLS

# Fill c => resultant value
c = []
for i in range(cROWS):
    c_col = []
    for j in range(cCOLS):
        c_col.append(0)
    c.append(c_col)

for i in range(aROWS):
    for j in range(aCOLS):
        for k in range(bCOLS):
            c[i][k] += a[i][j] * b[j][k]

print(c)
