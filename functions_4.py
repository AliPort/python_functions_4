#Write a Python function called max_num()to find the maximum of three numbers.
def maximum (a, b, c):
    list = [a, b, c]
    return max(list)

a= 36
b= 12
c = 15
print(maximum(a,b,c))

a= 35
b= 12
c= 1
print(maximum(a,b,c))

a= 113
b= 482
c= 238
print(maximum(a,b,c))


#Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(numbers):
    total= 1
    for x in numbers:
        total *=x
        return total
print(mult_list((4,2,9,7,3)))

#Write a Python function called rev_string() to reverse a string.

def my_statement(x):
    return x[::-1]

newText = my_statement("My new statement is now backwards!")
print(newText)



"""
Write a Python function called num_within() to check whether a number falls in a given range.
The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
"""
def num_within(n):
    if n in range(15,26):
        print( "%s is in the range"%str(n))
    else :
        print("The number is outside the given range.")

num_within(30)
num_within(17)




"""
Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
The function accepts the number n, the number of rows to print
Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
"""

def pascal_triangle(n):
   row = [1]
   y = [0]
   for x in range(max(n,0)):
      print(row)
      row=[l+r for l,r in zip(row+y, y+row)]
   return n>=1
pascal_triangle(6) 



