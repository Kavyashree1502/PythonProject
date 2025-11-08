# Logic Building

# Step Number-->1
#I/p--> num1=?, num2=? -->int
#O/P-->sum-->int, sub-->int, mult-->int, div--> float
num1 = int(input("Enter num1 value:"))
num2 = int(input("Enter num2 value:"))

print(type(num1))
print(type(num2))

# Step Number-->2
#Rough logic
# sum = +, sub = -, mult = *, div = /
# str-->int
# int()

# Step Number-->3
sum= num1+num2
sub= num1-num2
multi= num1*num2
div= num1/num2

print("sum is", sum)
print("sub is", sub)
print("multi is", multi)
print("div is", div)

