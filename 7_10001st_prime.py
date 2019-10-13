i=3
n=10001
if(n>=1):
    #print("Los primeros " +str(n) +" numeros primos son: ")
    print(2)
    
count=2
while(count<=n):
    c=2
    while(c<i):
        if(i%c==0):
            break
        c+=1
    if(c==i):
        if(count==10001):
            print(i)
        if(count%1000==0):
            print("lleva 1000")
        #print(i)
        count+=1
    i+=1
