def ksmallest(arr, k): 
    
    arr.sort() 
     
    return arr[k-1]

# Test 
arr = [1, 23, 12, 9, 30, 2, 50] 
k = 3
print(ksmallest(arr, k))