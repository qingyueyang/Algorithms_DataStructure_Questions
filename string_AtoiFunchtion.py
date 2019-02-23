def isNumericChar(x): 
    if (x >= '0' and x <= '9'): 
        return True
    return False
  
def myAtoi(string): 
    if len(string) == 0: 
        return 0

    res = 0    
    sign = 1         # initialize sign as positive 
    i = 0  

    # if number is negative then update sign 
    if string[0] == '-':    
        sign = -1
        i+=1
  
    # Iterate through all characters of input string and update result 
    for j in range(i,len(string)):         
        if isNumericChar(string[j] == False): 
            return 0
  
        res = res*10 + (ord(string[j]) - ord('0')) 
  
    return sign*res 


