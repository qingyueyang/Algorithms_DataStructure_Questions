def subArraySum(arr, n, Sum):  
   
    d = {}  
     
    curr_sum = 0 
    
    for i in range(0,n):  
       
        curr_sum = curr_sum + arr[i]  
        
                
        if curr_sum == Sum:  
           
            print("Sum found between indexes 0 to", i) 
            return 
           
    
        if (curr_sum - Sum) in d:  
           
            print("Sum found between indexes", 
            d[curr_sum - Sum] + 1, "to", i)  
              
            return 
            
        d[curr_sum] = i
            
    
    
    print("No subarray with given sum exists")  

arr = [10, 2, -2, -20, 10]
n = len(arr)
sum = -10
subArraySum(arr, n, sum)

1, 4, 20, 3, 10, 5
arr = [1, 4, 20, 3, 10, 5]
n = len(arr)
sum = 33
subArraySum(arr, n, sum)