# 27. Remove Element
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.


l1=[3,2,2,3] 
org=len(l1)
target=3 
out=[]
for i in l1:
    if i!=target:
        out.append(i) #2 2
    #  l1.pop(l1.index(i))
diff=org-len(out)
for i in range(diff):
    out.append("_")
print(out)