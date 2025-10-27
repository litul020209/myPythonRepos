s = "abcab"
start = 0
current = ""   
max_len = 0

for end in range(len(s)):
   
    if s[end] in current:
       
        while s[end] in current:
            current = current[1:]    
    
    
    current += s[end]
    
    
    max_len = max(max_len, len(current))

print("Longest length:", max_len)
