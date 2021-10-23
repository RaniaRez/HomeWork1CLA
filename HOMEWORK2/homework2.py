#1- read the file in one variable

file=open("C:\\Users\pc\Documents\HomeWork1CLA\HOMEWORK2\people.txt") 
people= file.read()
print(people)
###############################################################
#2- add a list of names to the file
people= people + "\nkarim don" +"\nmanel rahim"+"\nsihem ouagued"
file=open("C:\\Users\pc\Documents\HomeWork1CLA\HOMEWORK2\people.txt",'w')
file.write(people)
################################################################
#3- Read the first n lines of the file.

N =3 #you can change the number right here

file=open("C:\\Users\pc\Documents\HomeWork1CLA\HOMEWORK2\people.txt",'r')

with open("C:\\Users\pc\Documents\HomeWork1CLA\HOMEWORK2\people.txt") as myfile:
    head = [next(myfile) for x in range(N)]
print(head)

#####################################################################
#4- Read the last n lines of the file

c=3 #you can change the number right here
file=open("C:\\Users\pc\Documents\HomeWork1CLA\HOMEWORK2\people.txt",'r')
lines = file.readlines()
last_lines = lines[-c:]
print(last_lines)

#
name="emma johnson" #you can change the name right here
file=open("C:\\Users\pc\Documents\HomeWork1CLA\HOMEWORK2\people.txt",'r')
for line in file:
    if name not in line :
        trouv= False
    else:
        trouv=True
print(trouv)
#
for i in range(0,26):
    alphabet = chr(65+i)
    with open(f"{alphabet}.txt", 'w') as f:
        print(f"{alphabet}.txt")