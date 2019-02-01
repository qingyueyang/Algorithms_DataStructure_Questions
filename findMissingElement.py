def findMissing(arr, n): 
        
    x = 0
    for i in range(0, n): 
        x = x ^ (i+1) ^ arr[i] 
    x = x ^ (n+1) 

              
    return x 
      
# Test 
arr = [9, 8, 2, 1, 3, 5, 4, 7]  
n = len(arr)  
print("The missing element is", findMissing(arr, n)) 