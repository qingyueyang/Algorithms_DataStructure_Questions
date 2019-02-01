def findLeaders(arr, n): 
     
    curr_max = arr[n-1]    
    print(curr_max)    
    for i in range( n-2, 0, -1):         
        if curr_max < arr[i]:             
            
            curr_max = arr[i] 
            print(curr_max)
          
# Driver function 
arr = [16, 17, 4, 3, 5, 2] 
findLeaders(arr, len(arr)) 