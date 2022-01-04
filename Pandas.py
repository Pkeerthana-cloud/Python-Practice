import pandas as pd
std=pd.read_csv("Pandas/Students.csv")
print(std.head(4)) # returns first 4 records
print(std.tail(4)) # returns last 4 records

#csv tzble
import pandas as pd
std=pd.read_csv("Pandas/Students.csv")
print(std)

#tvs table
import pandas as pd
std=pd.read_csv("Pandas/Students.csv")
data=std.head(5)
print(data)
data.to_csv("Pandas/Students.csv",index=False)

