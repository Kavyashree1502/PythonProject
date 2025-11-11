# Tuple is a collection of items
# Syntax = ()
# Tuple are Immutable

# we can print empty tuple
t1 = ()
print(t1)

#conversion of list to tuple by using tuple ()

L1 = [1,2,3,4,5]
print(L1)
print(tuple(L1))

#tuple inside tuple

hero1 = (1,2,3,4,5)
print(hero1)

hero2 = (6,7,8,9,10)
print(hero2)

Hero = (hero1,hero2)
print(Hero)

print(Hero [0][0])
print(Hero [1][0])