def reverseString(s):
    def helper(s, start, end):
        if start == end:
            return s[start]
        
        return helper(s, start+1, end) + s[start]
    return helper(s, 0, len(s)-1)
    

print(reverseString("suresh"))

        
