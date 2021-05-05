# Given two strings s and t, check if s is a 
# subsequence of t.
# A subsequence of a string is a new string 
# that is formed from the original string by deleting some 
# (can be none) of the characters without disturbing the relative 
# positions of the remaining characters. (i.e., "ace" is a subsequence 
# of "abcde" while "aec" is not).
def isSubsequence(s, t):
    def helper(i, j):
        if i >= len(s):
            return True
            
        if j >= len(t):
            return False
            
        if s[i] == t[j]:
            return helper(i+1, j+1)
            
        return helper(i, j+1)

    return helper(0, 0)

print(isSubsequence("abc", "ahbgdc"))