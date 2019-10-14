import math
n=20000000000
A=[True]*(n+1)

for i in range(2,round(math.sqrt(n))+1):
    if A[i]:
        j=i*i
        while j<=n:
            A[j]=False
            j+=i
A[1]=False
suma=0
for a in range(len(A)):
    if A[a]:
        suma+=a

print(suma)
