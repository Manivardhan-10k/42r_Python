# sqrt 
# pow 
# floor 
# ceil 
# fabs 
# factorial
# gcd 
# lcm 


# pi e

# 100 -10
# sqrt # 10 

# 10.5   10 11
# import math as m
# num=123
# sqrt_val=m.sqrt(num) #10.0 
# if sqrt_val==m.floor(sqrt_val): #10.0   10
#     print("perfect square")
# else:
#     print("not perfect")

#random  #orderless 

#4  8912 6521 
    
import random as  r 
import math


#random
# val=r.random()  ## 0 -1   0.1 0.2 0.3  ...0.9
# print(math.ceil(val)) #1  1  1  1 1  0  0 0 0 0 0
# print(math.floor(val*10000))

# digits=4 
# otp=""
# for i in range(digits):#0 1 2 3    7642
#     num= math.floor(r.random()*10 ) # 
#     # otp=otp*10+num    ##7   7*10+6   76*10+4  764*10+2
#     otp+=str(num)   
# print(otp)
    

# print(r.randint(-100,5))



##uniform 
# print(r.uniform(2,5))

# choice
#list string tuple
# print(r.choice(["mahesh","AA","prabhas","PK"]))
# print(r.choice(("apple","mango","grapes","guava")))
# print(r.choice("abcdefghiklmnopqrstuvwxyz"))
# print(r.choice("0123456789")) 

#choices(seq,k=number)
# print(r.choices(["duke","r15","xl","luna","splendor"],k=2))

#sample 
# print(r.sample(("skoda","bmw","suzuki","tesla","rr"),k=5))


##shuffle 
# flowers=["rose","hibiscus","lilly","cauli flower"]
# r.shuffle(flowers)
# print(flowers)


#randrange 
# print(r.randrange(1,52,5)) #1 6 11 16 21 26 31 36 41 46 51


# 0/1   1    
# 2    10    
# 3    11
#4     100
#6     110
# print(r.getrandbits(3)) 


# random 
# randint 
# uniform 
# choice 
# choices 
# sample 
# shuffle 
# getrandbits
# ranrange