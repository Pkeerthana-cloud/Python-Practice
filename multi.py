#4.write  aprogram to print multiplicartion table of a given number
num = int(input( "/nEnter the number: "))
for count in range(1,11):
    print(num, 'x', count, '=', num*count)