#2 max valu
num_1 = int(input("How many integers would you like to enter?")) #enter an integer greater than or equal to 1
print("Please enter", num_1, "integers.")
_min = int(input())
_max = _min
for i in range(1, num_1):
   number = int(input()) #reads the integers one at a time
if number > _max:
   _max = number
if number < _min:
   _min = number