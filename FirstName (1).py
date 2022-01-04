#1a create a string made of the first, middle and last characters
str="Keerthana"
res=str[0]
l=len(str)
mi=int(l/2)
res=res+str[mi]
res=res+str[l-1]
print(res)