#1 min value
l=list(map(int,input("Enter array elements:").split(" ")))
min1=l[0]
for i in range(1,len(l)):
    if(l[i]<min1):
        min1=l[i]
print(min1)


