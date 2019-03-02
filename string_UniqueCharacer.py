def isUnique(str):
  if len(str) > 256:
    return False

  tracker = 0
  for char in str:
    val = ord(char)
    if (tracker & (1 << val)) > 0:
      return False
    tracker |= (1 << val)
  return True


#test
string = "122gGod"
print(isUnique(string))