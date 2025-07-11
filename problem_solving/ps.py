#sub string 
 
# name="mouli"
# #npvmj

# #ord  -- it returns the ascii of a char 
# #chr  -- it returns a char from the ascii 
# res="" 
# for i in name: #97 -122   108
#     code=ord(i)  # 
#     code+=1  #109
#     res+=chr(code)
# print(res)


# name="aravind"  # brbvjnd
# res=""
# for i in name: #a
#     if i in "aeiuoOIAEU":
#         res+= chr(ord(i)+1) #b
#     else:
#         res+=i
# print(res)
        


# if sub in word:
#     print(True)
# else:
#     print(False)
# word="baahubali"
# sub="bat"
# found=False
# for i in range(len(word)): #0 1 2 3 4 5 6 7 8
#     if sub==word[i:i+len(sub)]:
#         print(f" {sub} is a substring {word}")
#         found=True
#         break
# if found==False:
#     print("not a sub string")

#longest palindromic substring 

#aya 
#ala
#layal
# word="malayali" ##malayalam madam sos tat level radar racecar  amma akka anna mom wow dad sis bob
#ala 
#layal

# word="malayalam" # malayalam alayala ala aya  ala layal 
# longest="" #layal
# i=0
# while  i<len(word) and len(word[i::])>len(longest):  #4>5
#     temp=""
#     for j in range(i,len(word)):
#         temp+=word[j]
#         if temp==temp[::-1] and len(temp)>len(longest) :
#             longest=temp
#     i+=1
# if len(longest)>1:
#     print(longest)
# else:
#     print("no plaindromic substrings")    


# snake="python" # snake=snake.capitalize()  Python
# camel="Python Programme" # camel=camel.title().replace(" ","")
    
    

    