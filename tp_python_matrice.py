
def multiplication(A,B):
    '''A et B deux matrices '''
    nA = len(A) ; nB = len(B)
    pA = len(A[0])
    C = [[0 for j in range(nB)] for i in range(pA)]
    if nA != len(B[0]) :
        return 'multiplication impossible'
    for i in range (pA):
        for j in range(nB):
            for k in range(nA):
                C[i][j] += A[i][k] * B[k][j]
    return C



M=[[ 1,2 ],
[ 5,6 ]]



N=[[ 6,2 ],
   [ 8,2 ],
   [ 3,1 ]]
print (multiplication(M, N))
print (multiplication(N,M))