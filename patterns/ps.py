# patterns 

#designs  // shapes  

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# rows=5
# for i in range(1,rows+1):  #1 2 3 4 5  ---> for rows
#     res=""  #for storing the star in the row
#     for j in range(1,rows+1): #1 2 3 4 5 ## for columns
#         res+="*"+" "   # *****
#     print(res)
        
    
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# rows=5 
# for i in range(1,rows+1):# for rows   1 2 3 4 5
#     res=""  #for storing values in the row
#     for j in range(1,rows+1):  #for columns   1 2 3 4 5 
#         res+=str(j)+" " # 1 2 3 4 5
#     print(res)
        
        
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5 

# rows=5 
# for i in range(1,rows+1): #1 2 3  4 5
#     res=""
#     for j in range(1,rows+1):#1 2 3 4 5
#         res+= str(i) +" " #
#     print(res)
    

# *
# * *
# * * * 
# * * * *
# * * * * *
# rows=5
    
# for i in range(1,rows+1): #1 2 3 4 5 
#     res=""
#     for j in range(1,i+1): # 1 -2   1-3    1-4   1-5 1-6
#        res+="*"+" "
#     print(res) 



# * * * * *
# * * *
# * * 
# *
# rows=5 
# for i in range(rows,0,-1): #5 4 3 2 1
#     res=""
#     for j in range(1,i+1):
#         res+="*"+" "
#     print(res)



# * * * * * 
# *       *
# *       *
# *       *
# * * * * * 



# i==1  or i==rows  or j==1 or j==rows

# rows=5 
# for i in range(1,rows+1):   ##1  2 3 4 5
#     res=""
#     for j in range(1,rows+1):# 1 2 3 4 5 
#         if i==1 or i==rows  or j==1 or j==rows: # i2j1 i2j2 i2j3 i2j4 i2j5
#             res+="*"+" " #*  *
#         else:
#             res+=" "+" "
#     print(res)

# *       *
#   *   *
#     *
#   *   *
# *       *

            
# rows=5 
# for row in range(1,rows+1):
#     res=""
#     for col in range(1,rows+1):
#         if row==col or  row+col==rows+1:
#             res+="*"+" "
#         else:
#             res+=" "+" "
#     print(res)
    
# XOXOX
# OXOXO
# XOXOX
# OXOXO
# XOXOX


# rows=5 
# for row in range(1,rows+1):
#     res=""
#     for col in range(1,rows+1):
#         if (row+col)%2==0:
#             res+="X"+" "
#         else:
#             res+="O"+" "
#     print(res)

# * * * * * 
#     *
#     *
#     *
#     *

# rows=5 
# for i in range(1,rows+1):
#     res=""
#     for j in range(1,rows+1):
#         if i==1 or  j==(rows//2)+1:
#             res+="*"+" "
#         else:
#             res+=" "+" "
#     print(res)
        
# *       *
# *       *
# * * * * * 
# *       *
# *       *

# * * * * * 
# *
# * * * * * 
# *
# * * * * * 

# *       *
# * *     *
# *   *   *
# *     * *
# *       *

