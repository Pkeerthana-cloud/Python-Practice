#Remove empty strings from a list of strings
str_list = ["Keerthana", "Jahnavi", "", "Neeraj", None, "Harsha", ""]
res_list = []
for s in str_list:
    if s:
        res_list.append(s)
print(res_list)