  

     #        i        j         spaces
#     *       1        1           4  
#    * *      2        2           3
#   * * *     3        3           2
#  * * * *    4        4           1
# * * * * *   5        5           0

#rows=5    i=1 2 3 4 5         5-1= 4    5-2= 3     5-3= 2      5-4= 1     5-5=  0
# rows=5 
# for i in range(1,rows+1): 
#     res=""
#     for space in range(1,rows-i+1): #1-5  1-4   1- 3    1-2   1-1
#         res+=" "  #"    "
#     for j in range(1,i+1):
#        res+="*"+" "
#     print(res)



        #         i        j      spaces   rev
# * * * * *       1        5        0       5
#  * * * *        2        4        1       4
#   * * *         3        3        2       3  
#    * *          4        2        3       2
#     *           5        1        4       1

#rows=5   i= 5 4 3 2 1       5-5= 0   5-4= 1    5-3=  2      5-2=   3    5-1=  4
# rows=5
# for i in range(rows,0,-1):  
#     res=""
#     for space in range(1,rows-i+1):
#         res+=" "
#     for j in range(1,i+1):
#         res+="*"+" "
#     print(res) 

     #         i    j   spaces
#    1         1    1    3
#   2 3        2    2    2
#  4 5 6       3    3    1
# 7 8 9 10     4    4    0
# rows=int(input("enter the no of rows: "))
# num=1
# for i in range(1,rows+1):
#     res=""
#     for space in range(1,rows-i+1):
#         res+=" "
#     for j in range(1,i+1):
#         if num<10:
#             res+="0"+str(num)+" "
#             num+=1
#         else:
#            res+=str( num)+" "  ##1 
#            num+=1 
#     print(res)

#     a 
#    b c 
#   d e f 
#  g h i j 
# k l m n o 

# rows=5 
# asc=97
# for i in range(1,rows+1):
#     res="" 
#     for space in range(rows-i):
#         res+=" "
#     for j in range(i):
#         res+=chr(asc)+" "
#         asc+=1
#     print(res)
        



# * * * * *
# *
# * * * * *
#         *
# * * * * *
# rows=5 
# #i==1  i== rows  i==rows//2 +1   
# mid=(rows//2)+1  #3
# for i in range(1,rows+1) : 
#     res=""
#     for j in range(1,rows+1): 
#         if i<=mid:
#             if i==1 or j==1 or i==mid:
#                 res+="*"+" "
#             else:
#                 res+=" "+" "
#         else:
#             if i==rows or j==rows:
#                 res+="*"+" "
#             else:
#                 res+=" "+" "
#     print(res)
            
            
        
# * * * * *
#       *
#     *
#   *  
# * * * * * 
# i==1 i==rows i+j==rows+1

# *       *
#   *   * 
#     *
#     * 
#     * 
# i==j or i+j==rows+1 
# j==mid

# *       *
# * *   * *
# *   *   *
# *       * 
# *       * 
# j==1 or j==rows  i==j or i+j==rows+1 
# j==1 or j==rows