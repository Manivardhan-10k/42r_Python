# OOP 

#Object Oriented Programming 

# object based code   


#classes -> objects


#function oriented programming  

#includestdio.h 


# void main(){
    
# }


# num="hi"
# print(type(num)) 


# building --> design  -->blueprint 
#car-> fortuner ->
# blueprint -> 

#class 
# it is defined as a blueprint for object 


#attributes  and methods

class car:  
    brand="10K"
    def about(self):
        return "this is a car object"
    
    

# print(car)
# print(type(car)) 

# alto= car() 
# print(alto) 

# thar=car()
# print(thar)


# print(car.about(alto))
# print(thar.about())
# print(alto.about())


# r_42=car() 
# print(r_42.about())
# print(r_42.brand)

# class cls_name: 
#     attrbute=value 
#     def method(self): 
#         return
    
# name=cls_name()  

# class AC:
#     temp=20 
#     def cooling(self):
#         return " AC Cools the room" 
# ac1=AC() 
# print(ac1)
# print(ac1.temp)
# print(ac1.cooling())

# ac2=AC()
# print(ac2.temp,ac2.cooling()) 



class laptop: 
    def __init__(self,brand,ram,storage,processor):
        self.name=brand 
        self.ram=ram 
        self.storage=storage
        self.cpu=processor
    def specs(self):
        return f" {self.name} {self.ram} {self.storage} {self.cpu}"
            
        
# l1=laptop("HP",16,512,"i5")   
# # print(l1.name,l1.cpu)
# print(l1.specs())

# g1=laptop("ASUS",64,2,"i9")
# print(g1.specs())


# l1=laptop()
# # print(l1.brand)
# l2=laptop()
# # print(l2.brand)
# l3=laptop() 

