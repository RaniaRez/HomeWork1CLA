# 1- the list creation

Evenlst = []  #we declare a list 

for i in range(1,299): #the i will be in the interval 1 to 299
    
              
        if (i)%2 == 0:    #if the module of i and 2 is equal to 0 wwhich means i is an even number 
            
         Evenlst.append(i)    # i is stored in the list
       
print(Evenlst) #we print the list

#2- the length of the list
print(len(Evenlst))

#3- iteration through the list
for i in Evenlst :
    print("the square of",i, "is ",i**2 )


#4- check if 57 is in the list 
print(57 in Evenlst)
