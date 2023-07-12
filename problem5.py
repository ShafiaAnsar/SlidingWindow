 #Longest Substring Without Repeating Characters 
 #leetcode problem medium
class Solution:
    def lengthOfLongestSubstring(self,s:str)->int:
        left = 0
        max_len= 0
        charSet = set()
        for r in range(len(s)):
            if s[r] not in charSet:
                charSet.add(s[r])
                max_len = max(max_len, r-left+1)
            else:
                while s[r] in charSet:
                     charSet.remove(s[left])
                     left+=1
                charSet.add(s[r])
        return max_len

