# OOP :
# object oriented programming 

# --> everthing is a object 

# object --> it is a real value/entity 


#dog -- class
# ->tail, four legs ,bow bow   

# middle class 

# 20-25k 
#wife - 2kids 
#chetak scooter 
#rich class -dream    




# car  

# sports 
# suv 
# hatchback 
# sedan 

# class -- a blue print to create object  (blueprint/reference) 

#object  -->is an instance of a class


# python  
# n1=int("1")
# print(id(n1))


#int -class 
#n1 - instance  


# OOP   vs  FOP(Funtion Oriented Programming) 



# void main(){
    
# }  


# class laptop:
#     ram="24gb" 
#     cpu="i5"
#     storage="512gb"  
#     def is_working(self):
#         return "laptop is working properly"
# #properties /attributes 
# #methods 
# l1=laptop()
# l2=laptop()
# l3=laptop()
# l4=laptop()
# print(l4.is_working())


class laptop:
    brand="hp" 
    #constructor
    # it is a special method which is executed automatically ,when a instance is  created 
    def __init__(self,cpu,ram,storage,gpu): 
        self.ram=ram 
        self.cpu=cpu 
        self.storage=storage 
        self.graphics=gpu 
    def update_laptop_ram(self,val):
        self.ram=val
        
        
# victus=laptop("i9","64gb","4tb","rtx5050")
# print(victus.ram)
# print(victus.storage) 
pavillion=laptop("i7","32gb","1tb","rtx3050")
print(pavillion.ram)
pavillion.update_laptop_ram("128gb")
print(pavillion.ram)


# display
# ram 
# storage 
# battery 
# processor
    
    

    
    

    