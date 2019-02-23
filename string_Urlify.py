def spaceReplace(str):
    strArr = list(str)
    for i, c in enumerate(strArr):
        if c == ' ':
            strArr[i] = '%20'
    
    return ''.join(strArr)

str = 'winter is coming'
print(spaceReplace(str))