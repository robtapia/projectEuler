import math

def iterar(i):
    for j in range(1,20):
        if((i%j)!=0):
            return False
    return True

maximo=math.factorial(20)
for i in range(1,maximo):
    if(i%100000==0):
        print(i)
    if (not iterar(i)):
        continue
    break
print(i)
            
