def search(arr, n, key): 
  
    # Travers the given array starting 
    # from leftmost element 
    i = 0
    while (i < n): 
      
        # If key is found at index i 
        if (arr[i] == key): 
            return i 
  
        # Jump the difference between 
        # current array element and key 
        i = i + abs(arr[i] - key) 
      
    print("key not found!") 
    return -1
  
# test 
arr = [8 ,7, 6, 7, 6, 5, 4, 3, 2, 3, 4, 3 ] 
n = len(arr) 
key = 3
print("Found at index ", search(arr,n,key)) 