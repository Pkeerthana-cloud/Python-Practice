#3.Write a Python program to print the current date and time
import datetime
now=datetime.datetime.now()
print("currwnt date and time: ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))