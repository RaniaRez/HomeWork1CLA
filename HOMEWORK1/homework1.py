#1
LST = [] 
for i in range(1, 299):  # go through all numbers 1-299 
    if i % 2 == 0:  # check if number is divisible by 2 
        LST.append(i)  # if so, add to the list 
print(LST)

#2

length=LST.len()
print("the length of our list is", length)

#3
for i in LST:
       print("the squared of ",i, "is",i**2)


#4
exist= 57 in LST
print("the statement 57 exists in the list is", exist)

