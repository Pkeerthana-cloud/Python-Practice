#15Use a loop to display elements from a given list present at odd index positions
list=[1,2,3,4,5,6,7,8,9]
for i in list[1::2]: #using list slicing
    print(i, end=" ")