# list is a collections of items
# Allows duplicates
#Syntax = []
#List starts from zero index
# Allows multiple different data types of elements
# It can store 0 to Length - 1 elements
#List is mutable (It can be updated / vale can be changed)

My_List = [1,2,3]
print(My_List)
print(My_List[0])
print(len(My_List))

#Indexing
My_List[0] = "Kavya"
print(My_List)

# Append

My_List.append(5)
print(My_List)

#extend
My_List.extend([8,9,2, 6,8,1])
print(My_List)

#insert
My_List.insert(0,"Amit",)
print(My_List)

#Remove
My_List.remove("Amit")
print(My_List)

#pop
print(My_List.pop())
print(My_List)

My_List.remove("Kavya")
print(My_List)

# sort
# Sort can only be used for same data type
My_List.sort()
print(My_List)

