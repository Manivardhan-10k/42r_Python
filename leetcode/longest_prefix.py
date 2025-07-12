# 14. Longest Common Prefix
# Easy
# Topics
# premium lock icon
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "". 



# Example 1:

# Input: strs = ["flower","flow","slowing"]   
# Output: "flo"
# class Solution(object):
def longestCommonPrefix( strs):
        """
        :type strs: List[str]
        :rtype: str
        
        """
        smallest=strs[0]  ##flower
        res="" 
        for i in strs:
            if  len(i)<len(smallest):
                smallest=i 

        stop=False 
        for j in range(len(smallest)):  # 0 1 2 3 
            for i in strs: ##"flower"
                if smallest[j]==i[j]:
                    pass       
                else:
                    stop=True
                    break       
            if stop:
              break
            else:
                res+=smallest[j]
        return  res
print(longestCommonPrefix(["flower","flow","flying"]  )) 
                    
                    
            
                
            
        
                
        
        
        