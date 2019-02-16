def sortByFreq(arr):    
    #create a dictionary
    d = {}  
    for i in arr:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    
    # sort the dictionary
    d1 = sorted(d.items(),key=lambda item:item[1],reverse=True)

    newArr = []
    for item in d1: 
      newArr.extend([item[0]] * item[1])
    print(newArr, sep = ',')

arr =[2, 5, 2, 8, 5, 6, 8, 8]
sortByFreq(arr)