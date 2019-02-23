def strStr(s, x):
        
        if not x:
            return 0
        for i in range(len(s) - len(x) + 1):
            if s[i] == x[0]:
                j = 1
                while j < len(x) and s[i+j] == x[j]:
                    j += 1
                if j == len(x):
                    return i
        return -1

s = 'wednesday'
x = 'day'

print(strStr(s,x))
