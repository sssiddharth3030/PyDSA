#medium.com/@abasaeed/understanding-hash-maps-hash-tables-and-hash-sets-in-python-c0a78b1e131


# Hashing is a technique used in computer science to efficiently store and 
# retrieve data. It involves converting data (such as strings or numbers) 
# into fixed-size values called hash codes. 

# These hash codes are used as indexes to store the data in data structures
# like hash maps, hash tables, and hash sets.

# HASH MAP / HASH TABLE
# Hash map and a Hash table are both the the same they ways to store and organize 
# information so we can find it quickly .

# And we can implement them using dictionary in python

# Creating a hash table to store fruits based on their first letter
hash_table = {}
hash_table['A'] = 'Apple'
hash_table['B'] = 'Banana'
hash_table['O'] = 'Orange'

# Accessing a fruit based on its first letter
for i in hash_table:
    print(i, hash_table[i])

hash_table.pop('O', None)

if 'O' in hash_table:
    print(hash_table['O'], 'exists')  # Output: 'Orange'
else:
    print("Key 'O' does not exist")


print(hash_table)

# HASH SET
# Similar to hash table, a hash set is also a collection of objects. 
# In hash table, data was stored in the form of key-value pairs, 
# whereas in hash sets, the data is stored as objects .
# A hash set also does not allow storage of duplicate elements.

# Hash Set
my_hash_set = set()

# Adding elements to the hash set
my_hash_set.add(3)
my_hash_set.add(7)
my_hash_set.add(1)
my_hash_set.add(9)
my_hash_set.add(5)

# Searching for an element in the hash set
search_element = 7
if search_element in my_hash_set:
    print("Element found in the hash set!")
else:
    print("Element not found in the hash set.")
    
my_hash_set.remove(3) #will raise error if no key found
my_hash_set.discard(3) #will not raise error if no key found

print(my_hash_set)