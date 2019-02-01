def searchMagicIndex(arr, first, last): 
    if first > last: 
        return -1

    if last >= first: 
        mid = (first + last)//2
      
    if mid == arr[mid]: 
        return mid 
      
    if mid > arr[mid]: 
        return searchMagicIndex(arr, (mid + 1), last) 
    else: 
        return searchMagicIndex(arr, first, (mid -1)) 
      
    # Return -1 if there is no Magic index 
    return -1
  
  
# test arry  
arr = [-10, -1, 0, 3, 10, 11, 20, 30, 40] 
n = len(arr) 
print("Magic index is ", searchMagicIndex(arr, 0, n-1)) 