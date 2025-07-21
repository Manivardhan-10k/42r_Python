      #       i    j    spaces
#     *       1    1      4
#    * *      2    2      3
#   * * *     3    3      2
#  * * * *    4    4      1
# * * * * *   5    5      0
#  * * * *    4    4       1
#   * * *     3    3       2
#    * *      2    2       3
#     *       1    1       4

#rows=5   i= 1 2 3 4 5          5-1= 4    5-2=3   5-3=2   5-4= 1   5-5= 0   
#138
# rows=5
# for i in range(1,rows+1):
#     res=""
#     for space in range(rows-i):
#         res+=" "
#     for j in range(i):
#         res+="*"+" "
#     print(res) 

# # rows=5     i= 4 3 2 1               1 2 3 4
# for i in range(rows-1,0,-1):
#     res=""
#     for sp in range(rows-i):
#         res+=" "
#     for j in range(i):
#         res+="*"+" "
#     print(res)
    


      #       i    j    spaces
#     *       1    1      4
#    * *      2    2      3
#   * * *     3    3      2
#  * * * *    4    4      1
# * * * * *   5    5      0
#  * * * *    6    4      1
#   * * *     7    3      2
#    * *      8    2      3
#     *       9    1      4

#i<=rows
#rows=5 i= 1 2 3 4 5    rows-i        4 3 2 1 0
#rows=5   i= 6 7 8 9     i-rows         6-5= 1  7-5=2 8-5=  3   9-5= 4

#i<=rows 
#   i
# rows=5 i= 6 7 8 9         4 3 2 1    rows*2-i  10-6  10-7   10-8 10-9                                        i-(2*spaces) 
# rows=5 
# for i in range(1,2*rows):
#     res=""
#     cols= i if i<=rows else  rows*2-i                    #i-(2*spaces)
#     spaces= rows-i if i<=rows else i-rows
#     for space in range(spaces):
#         res+=" "
#     for j in range(cols):
#         res+="*"+" "
#     print(res)
        
        
# rows=5 
# for i in range(1,2*rows):
#     spaces= rows-i if i<=rows else i-rows 
#     cols= i if i<=rows else (rows*2 )-i 
#     print((" "*spaces)+("* "*cols))
    
      #        i      j     spaces
# * * * * *    1      5      0
#  * * * *     2      4      1
#   * * *      3      3      2
#    * *       4      2      3
#     *        5      1      4
#    * *       6      2      3
#   * * *      7      3      2
#  * * * *     8      4      1
# * * * * *    9      5      0



#rows=5  i=  6  7 8 9    3  2   1    0   2*5-6-1 =3    2    10-8-1  1   10-9-1 0

#rows=5  1 2 3  4 5          5 4 3 2 1   rows-i+1 5-1+1=5  5-2+1 4  5-3+1    5-4+1  5-5+1 

# rows=5  i= 6 7 8 9      2  3  4   5  6-5+1   7-5+1    8-5+1  9-5+1
# rows=5 
# for i in range(1,2*rows):
#     spaces= i-1 if i<=rows else 2*rows-i-1
#     cols= rows-i+1 if i<=rows else i-rows+1 
#     print((" "*spaces)+("* "*cols))


#      a 
#     b c 
#    d e f
#   g h i j 
#  k l m n o 
#   p q r s
#    t u v
#     w x 
#      y

# rows=5
# code=97
# for i in range(1,2*rows):
#     res=""
#     spaces= rows-i if i<=rows else i-rows 
#     cols= i if i<=rows else 2*rows-i 
#     res+= (" "*spaces)
#     for j in range(cols):
#         res+=chr(code)+" "
#         code+=1
#     print(res)        


# word="aaaaaaaaaaaaaaaaa" #a   
# longest=""
# char=word[0] #a 
# if word.count(char)==len(word):
#     longest=char
# else:
#     for i in range(len(word)):
#      temp=""
#      for j in range(i,len(word)):
#         if word[j] not in temp:
#             temp+=word[j]
#         else:
#             if len(temp)>len(longest):
#                 longest=temp  
#             break
# print(longest)

# "aabbcccaabbcccd" "a2b2c3a2b2c3d1" 


write the programmes to print the following patterns
1 
1 2
1 2 3
1 2 3 4 
1 2 3 4 5


* * * * * 
* *   * *
*   *   *
* *   * * 
* * * * * 


       1 
     2 3
   4 5 6
7 8 9 10


*       * 
* *   * *
*   *   *
*       * 
*       * 


*
* *
* * * 
* * * *
* * * * *
* * * *
* * * 
* *
* 