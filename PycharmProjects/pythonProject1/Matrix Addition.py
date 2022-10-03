A = [[1,2,3],
     [3,2,1],
     [1,3,2]]

B = [[1,1,1],
     [1,1,1],
     [1,1,1]]

e = 0
r = 0
u = []
for a in A:
    r = 0
    u.append([])
    for q in a:
        y = A[e][r] + B[e][r]
        u[e].append(y)
        r = r+1
    e = e + 1

print(u)
