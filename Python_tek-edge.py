# Variable declaration
x = 10

# Data types - int, float, boolean, string, 
type(x)  # int

####################################################
# Data strictures - list, tuples, set, dictionary, 
#####################################################

########## list - 0 indexing, slicing, mutable objects
l1 = [10,20,30,'xx','yy']

# slicing - [inclusive:exclusive:step]
l1[2]
l1[-2]
l1[1:2]

# inserting / append / extend

l1.append(2) - # only for single element
l1.extend([1,2,3]) - # onlty for multiople elements
l1.insert(2,85) - # to insert element at specific position

# count / len
len(l1)
l1.count('yy')

# pop / remove
l1.pop() # removes the last element and returns it 
l1.remove('yy') # removes the last element

# sort / sorted
l1.sort()
sorted(l1, reverse = True)

########## Dictionary
# keys - can be integers or strings

dict = {}
type(dict)
dict1 = {'key1': 'a',
          2:2,
          '3':3}
dict1.keys()
dict1.values()
dict1.items()
dict1['key1']

# updating
dict1.update({'key3':4,'key5':5})

########### Tuple


