# abstraction
#hiding the implementation details and showing what is necessary 
#abstract-art 


# from abc import ABC ,abstractmethod 


# #concrete class
# class Device(ABC):  ##inheriting
#     @abstractmethod  ##decorator
#     def welcome(self):
#         pass 


# #marriage 
# ##they add additional functionality without modifying the original function 

# class Mobile(Device):
#     def welcome(self):
#         pass
      
# m1=Mobile()
# print(m1)


# class gp :
#     pass 
# class p(gp):
#     pass 
# class child(p):
#     pass 


#single inheritance
#a parent class should have only  a single child class 


#multiple inheritance 
# a child class having mulitiple parent classes

# class father():
#     money=100000 
# class mother():
#     food="biryani" 

# class child(father,mother):
#     pass 
# c1=child()
# print(c1.money)
# print(c1.food) 


##hierarchial inheritance
#a parent class having multiple child classes  



#hybrid inheritance 
# a combination of multiple types of inheritance 

# class A :
#     name="A" ##property /attribute 
# class B():
#     # pass
#     name="B"
# class C():
#     # pass
#     name="C" 
# class D(B,C):
#     pass 
# obj_d=D()
# print(obj_d.name) 
 
 



#MRO  
#Method Resolution Order

    
# print(D.mro())

# single 
# multiple 
# multi level 
# hierarchial 
# hybrid 
#MRO 



#recursion 
# a function calling itself 

#factorial 
# num=5 #120 
#5*4*3*2*1 

# def factorial(n): #5 
#     if n==1:
#         return 1 
#     else:
#         return n*factorial(n-1)##5*factorial(5-1)*factorial(4-1)*facorial(3-1)*factorial(2-1)
     
# print(factorial(num)) 
# print(factorial(5))
    
    
# login    ---> show reels

# def login():
#     # return False 
#     print(True)


# def show_reels():
#     if login():
#         print("show reels")
#     else:
#         print("login first")
# show_reels()   



#call back
# def add_num(m,n):
#     return is_even(m+n)
# def is_even(a):
#     print(a%2==0) 
# add_num(5,2) 

# lambda --> it 

# some=lambda : "hello"
# print(some())

# addition=lambda x,y : x+y
# print(addition(2,3))