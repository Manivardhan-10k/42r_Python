# file handling 

#CRUD
#Create 
#Read 
#Update 
#Delete 

#text files -- .txt 

#OS -- operating System  

#programming languages 

#open(file,mode)  

# file=open("./sample.txt","r")  ##accessing the file
# print(file.read())  ##to read the content in the file 
# print(file.readline())# it reads  a single line
# print(file.readline())
# print(file.readline())
# print(file.readline()) 


#readlines()  -- this returns a list of each line as a element
# print(file.readlines()[-1])  



# file=open("./sample.txt","w")
# file.write("this is added from the python file")

# file=open("./sample.txt")
# print(file.read())


# file=open("sample2.txt","w") 
# file.write("this is for the second file")



# file=open("sample2.txt","w")
# file.writelines(["first\nline\n","second\n","third\n"])
# file.close()
#escape characters 
#\n \t \b \r


#seek  
# file=open("sample.txt")
# # file.seek(7)
# # print(file.tell())
# print(file.read())


#truncate 
# f = open('./sample.txt', 'r')
# f.truncate(5)
# print(f.read()) 


# with open("sample.txt","r") as file:
#     print(file.read())  

# with open("sample.txt","a") as file:
#     file.write("\nwelcome to class")
#     file.write("\nwelcome to python class")
    
# with open("sample.txt","w") as file:
#     file.write("") 

with open("sample.json","w") as file:
    file.write('"msg":"hello"')