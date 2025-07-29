# OOPS: 
# class --> it is a blueprint for creating objects 
# object-> it is an instance of a class  
# num=1 
# print(type(1))
#is_instance 
# print(isinstance(1,int))
# print(isinstance(1,str))
# print(isinstance((),list))
# print(isinstance((),tuple)) 

# class Mobile: 
#     brand="SAMSUNG"   ##attributes/properties 
#     #brand---> class attribute/variable/property 
#     # every object will have same class variables
#     def __init__(self,model,ram,storage,camera,display,price):
#         self.model=model 
#         self.ram=ram 
#         self.rom=storage
#         self.cam=camera 
#         self.screen=display 
#         self.cost=price
#         ##instance variables /properties
#     def about(self):
#         return f"this is {self.model} mobile"
        
# m5=Mobile("s24","12gb","512gb","200MP","4k","1.5")   
# print(m5.brand)  
# print(m5.cam)

# m6 =Mobile("m21","6gb","128gb","48MP","fhd","20k")
# print(m6.brand)
# print(m6.cam)
        
    
    
# s24=Mobile()
# print(s24.brand)
# m24=Mobile()
# print(m24.brand)


# oops:
# class 
# object 
# inheritance 
# abstraction 
# encapsulation 
# polymorphism 


##getting the properties of parent class in the child class 

# class Animal:
#     legs=4 
#     tail=1 

# # dog=Animal()
# # print(dog.legs)
# # cat=Animal()
# # print(cat.legs)
# class Dog(Animal):#parent is defined in ()
#     sound="bow bow" 
# d1=Dog()
# print(d1.sound)
# print(d1.legs)


# class Cat(Animal):
#     sound="meow meow" 
# c1=Cat()
# print(c1.legs) 

# class Monkey(Animal):
#     legs=2 
#     hands=2 

# m1=Monkey()
# print(m1.legs)
# print(m1.hands)

##multi-level inheritance
# class GrandParent:
#     prop=1000 
#     gp="appalnaidu"
# class Parent(GrandParent):
#     prop=10000 
#     pn="naidu"
# class Child(Parent):
#     prop=0  
#     name="aravind" 
# class GrandChild(Child):
#     pass



# child1=Child() 
 
 
# parent1=Parent()
# print(parent1.pn)
# print(parent1.gp)
# print(parent1.name)
    
# gc1=GrandChild()
# print(gc1.name)    

#polymorphism 
#poly -many/multiple  morphism-forms 
class Animal:
    def sound(self):
        return "this animal makes some sound"
class Dog(Animal):
    def sound(self):
        return "this animal makes bow bow sound"  
class Cat(Animal):
    def sound(self):
        return "this animal makes meow meow sound" 

d1=Dog()
print(d1.sound()) 
c1=Cat()
print(c1.sound()) 


# class variables
# instance variables  
#isinstance
#inheritance 
#accessing the parent properties in the child class
#we can't access child properties in parent class
#polymorphism 
#same method working differently in different classes 


# encapsulation: 
    
#wrappin the methods and variables into a  single unit

