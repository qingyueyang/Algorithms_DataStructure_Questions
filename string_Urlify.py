def spaceReplace(s):
    str = ""
    for x in s:
        if x == " ":
            str += "%20"
        else:
            str += x
    return str

str = 'winter is coming'
print(spaceReplace(str))