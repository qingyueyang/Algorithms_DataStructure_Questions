def findDuplicate(arr, n): 
        
    x = 0
    for i in range(0, n-1): 
        x = x ^ (i+1) ^ arr[i] 
    x = x ^ arr[n-1] 

    if x >= n:
        return -1
          
    return x 
      
# Test 
arr = [9, 8, 2, 6, 1, 6, 5, 3, 4, 7]  
n = len(arr)  
print("The duplicate is", findDuplicate(arr, n)) 