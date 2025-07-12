
# Code
# Testcase
# Testcase
# Test Result
# 21. Merge Two Sorted Lists
# Easy
# Topics
# premium lock icon
# Companies
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.


l1=[1,3,4] 
l2=[] 
out=[]


if len(l1)==len(l2):
    for i in range(len(l1)):
        if l1[i]>l2[i]:           
          out.append((l2[i]))
          out.append((l1[i]))
        else:
          out.append((l1[i]))
          out.append((l2[i]))
if not l1 and l2:
    out=l2
if len(l2)==0 and len(l1)>0 :
    out=l1
else:
    out=[]
            

    



