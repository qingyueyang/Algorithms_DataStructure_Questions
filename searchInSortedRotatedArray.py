def search (arr, first, last, target): 
    if first > last: 
        return -1
      
    mid = (first + last) // 2
    if arr[mid] == target: 
        return mid 
  
    # If arr[first...mid] is sorted  
    if arr[first] <= arr[mid]: 
  
        # As this subarray is sorted, we can quickly 
        # check if target lies in this half or other half  
        if target >= arr[first] and target <= arr[mid]: 
            return search(arr, first, mid-1, target) 
        return search(arr, mid+1, last, target) 
  
    # If arr[first..mid] is not sorted, then arr[mid... last] 
    # must be sorted 
    if target >= arr[mid] and target <= arr[last]: 
        return search(arr, mid+1, last, target) 
    return search(arr, first, mid-1, target) 
  
# Test 
arr = [4, 5, 6, 7, 8, 9, 1, 2, 3] 
target = 2
i = search(arr, 0, len(arr)-1, target) 
if i != -1: 
    print ("Index:", i) 
else: 
    print ("Target not found") 
  
