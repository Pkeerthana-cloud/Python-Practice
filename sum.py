#calculate the sum of all numbers from i to a given number
n =int(input("Enter the number: "))
sum=0
for num in range(1,n+1,1):
    sum=sum+num
    print("Sum of first ", n, "numbers is: ", sum)
average = sum / n
print("Average of ", n, "numbers is: ", average)   



