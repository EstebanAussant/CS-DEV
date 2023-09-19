M=[[ 1,2 ],
[ 5,6 ]]

N=[[ 6,2 ],
   [ 8,2 ],
   [ 3,1 ]]


def multiplication(A,B):
    nA = len(A) ; nB = len(B)
    pA = len(A[0])
    C=[]
    if nA != len(B[0]) :
        return 'multiplication impossible'
    for i in range (pA):
        for j in range(nB):
            for k in range(nA):
                C[i:j] += A[i][k] * B[k][i]
    return C


print (multiplication(M, N))
print (multiplication(N,M))