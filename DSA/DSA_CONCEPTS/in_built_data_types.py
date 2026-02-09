# static arrays, dynamic arrays and strings

# LIST
A = [1,2,3,4]

# Append - Insert the element at the end of the array - O(1)
A.append(5)
print(A)

# Insert at some position in the array - O(n)
A.insert(2, 10)
print(A)

# Modify an element in an array - O(1)
A[2] =222
print(A)

# Accessing an element at the given index i
print(A[2])

# Deleting an element at the end of the array O(1)
print(A.pop())

# Check if an array has an element O(n)
if 222 in A:
    print("found")
else:
    print("Not found")

# Checking length - O(1)
print("Length - ", len(A))

# STRINGS

# Append to the end of the string
str1 = "Hello World !"
str2 = str1 + " Nitin :) "
print(str2)

# Check if something is in the string
if "World" in str2:
    print("world found")
else:
    print("Nothing found")

# Checking length in string - O(1)
print("str1 lenght - ", len(str1))
print("str2 lenght - ", len(str2))



