sumsquare=0
squaresum=0
for i in range(1,101):
    print(i)
    sumsquare=sumsquare+(i*i)
    squaresum+=i

squaresum=squaresum*squaresum
print(sumsquare-squaresum)
