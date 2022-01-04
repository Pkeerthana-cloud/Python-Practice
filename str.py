for row in range(7):
   for col in range(7):
     if row==0 and col%3!=0 or row==1 and col%3==0 or row-col==2 or row+col==8:
        print(" * ",end=" ")
     else:
        print(" ",end=" ")
        print()
        
#
str1= input("Enter string")
str2= input("Enter string")
count=0
for i in range(len(str1)):
    if str1[i]==str2[i]:
        count=count+1
        print(count)
        
#
for i in range(50,500,1):
    print(i)
else:
    print(i)
