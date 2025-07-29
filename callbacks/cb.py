# callback: 

# a function passed as a parameter or used inside a function 



# def addition(a,b,fun): ##1 b=2  fun=is_even  (callback)
#     return  fun(a+b)

# def is_even(n):
#     return n%2==0
    
# print(addition(12,2,is_even)) 

#Higher order function
# a function which takes another function as a paremeter or 
# a functio  which returns a function  or both 
    


# map 
# filter 
 
# l1=[1,2,3,4,5,6]  #[2,4,6,8,10,12]
# out=[]
# for i in l1:
#     out.append(i*2)
# print(out)  


# l1=[1,2,3,4,5,6]  #[2,4,6,8,10,12]
# def multiply(n):
#     return n%2==1
    
# print(list(map(multiply,l1)))  ##multiply -callback  map--hof 

# #filter 

# print(list(filter(multiply,l1))) 



# l1=["ganesh","aravind","savithri","srivalli"]
# print(list(filter(lambda x :len(x)>=6,l1)))
# print(list(map(lambda y :len(y)<=6,l1))) 


# students=[
#     {"marks":250},
#     {"marks":300},
#     {"marks":450},
#     {"marks":500}
#     ]

# student=map(lambda x : x["marks"]>=500,students )
# print(list(student)) 

# ele=["hi",1,{"name":"mani"},"hello",True, None,(4,5,6) ,[1,2,3],"world",False]
# print(list(filter(lambda x : isinstance(x,str) or isinstance(x,int),ele))) 


#callback 
#HOF 
#map 
#filter 

ele=[5,4,6,9,78,7]
print(list(map(lambda x :x%2==0,ele)))