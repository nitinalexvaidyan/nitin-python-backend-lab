# Hash tables, Hash functions, sets and maps
'''
Hashable (immutable objects) -> strings, integers, tuples, frozen sets
Non Hashable (mutable objects) -> list, dict, etc
'''

# __________ Hash sets __________
s = set()
print(s)

# add item into set - O(1)
s.add(1)
s.add(2)
s.add(3)
print(s)

# Loop if an item is in the set - O(1)
if 1 in s:
    print("present")
else:
    print("absent")

# Remove an item from the set - O(1)
if 3 in s:
    s.remove(3)
print(s)

str1 = "aaaabbbbbcccccdddd"
set1 = set(str1)
print(set1)

# Looping in set - O(n)
for item in s:
    print(item)


# __________ Hashmaps - Dictionaries __________
d = {"nitin": 1, "theja": 2, "ethan": 3}
print(d)

# Add key: val in dict - O(1)
d["esther"] = 4
print(d)

# Check for presence of a key in a dict - O(1)
if 'nitin' in d:
    print("present")
else:
    print("absent")

# Check the value corresponding to a key in the dict - O(1)
print(d["ethan"])

# Loop over key value pairs - O(n)
for key, val in d.items():
    print(key, val, sep=" ")


# __________ Default dict __________
from collections import defaultdict
default = defaultdict(dict)
default[2]
print(default[3])
print(default)


# __________ Counter __________
from collections import Counter
counter = Counter(str1)
print(counter)