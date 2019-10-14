trios=[]
for a in range(500):
    print(a)
    for b in range(500):
        for c in range(500):
            if ((a*a)+(b*b)==(c*c)):
                trios.append([a,b,c])

#print(len(trios))
print("ahora reviso los trios")

for trio in trios:
    if trio[0]+trio[1]+trio[2]==1000:
        print("Lo encontre!")
        print(trio)
print("falle")
