def arePermutation(str1, str2):
  count = [0]*256
  if len(str1) != len(str2):
    return False

  for i in str1:
    count[ord(i)]+=1

  for i in str2:
    count[ord(i)]-=1
    
  for i in range(256):    
    if count[i] != 0:   
       
      return False
  
  return True

str1='abcb'
str2='abcc'
print(arePermutation(str1,str2))