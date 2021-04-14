def reverseString(s):
    # Complexity is O(N)
    # Space complexity: Recursion stack. O(N)
    def helper(s, start, end):
        if start < end:
            s[start], s[end] = s[end], s[start]
            helper(s, start+1, end-1)
        
    helper(s, 0, len(s)-1)
    return s

print(reverseString(list("suresh")))