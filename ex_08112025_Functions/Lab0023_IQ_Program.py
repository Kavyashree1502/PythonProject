# Create a program to sum of three number from the user input,
# If user does not enter any number, use default as 100, 200, 300

num1 = int(input("Enter a num1 value\n"))
num2 = int(input("Enter a num2 value\n"))
num3 = int(input("Enter a num3 value\n"))

def sum_of_three(n1=100, n2=200, n3=300):
    return n1 + n2 + n3

result = sum_of_three(num1, num2, num3)

result2 = sum_of_three()
print(result2)


