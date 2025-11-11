# Syntax - Lambda arguments : expression

# Lambda is used to optimize the code. It always return the function, so we call the function

# example 1

result = lambda x,y:x+y
print(result(1,2))

# example 2
#Write a program to check even and odd

check_even_odd = lambda n:"Even" if n%2==0 else "odd"
print(check_even_odd(8))