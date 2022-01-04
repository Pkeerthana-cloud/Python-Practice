#1b. Create a string madde of the middle three characters
def get_middle_three_chars(str):
    mi=int(len(str)/2)
    res = str[mi - 1:mi + 2]
    print("Middle three chars are:", res)
get_middle_three_chars("KeerthanaSai")
get_middle_three_chars("Jahnavisai")