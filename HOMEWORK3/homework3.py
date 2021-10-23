#1
def isPalindrome(string):
	left_pos = 0
	right_pos = len(string) - 1
	
	while right_pos >= left_pos:
		if not string[left_pos] == string[right_pos]:
			return False
		left_pos += 1
		right_pos -= 1
	return True
print(isPalindrome('coc'))

#2
def isPrime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True          
print(isPrime(5))        

#3
def isinrange(n):
    if n in range(2,100):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
isinrange(10)

#4
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("give the number to calculate the factiorial : "))
print(factorial(n))

#5
def string_reverse(str1):

    rstr = ''
    index = len(str1)
    while index > 0:
        rstr += str1[ index - 1 ]
        index = index - 1
    return rstr

print(string_reverse('rania'))
#6
def sum(numbers):
    somme = 0
    for x in numbers:
        somme += x
    return somme
print(sum((2, 2, 5, 0, 9)))