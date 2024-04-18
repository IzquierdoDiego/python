#Lists

colores = ['rojo', 'verde', 'Azul']

print(colores)

colores_copy = colores # dont creeate a new list, make reference to same one

print(colores_copy)

colores[0] = 'purple'

print(colores_copy)


for color in colores:
	print(color)

print()

if 'purple' in colores_copy:
	print('color in the list')
	
## print the numbers from 0 through 99
for i in range(7):
  print(i)

"""
list.append(elem) -- adds a single element to the end of the list. Common error: does not return the new list, just modifies the original.
list.insert(index, elem) -- inserts the element at the given index, shifting elements to the right.
list.extend(list2) adds the elements in list2 to the end of the list. Using + or += on a list is similar to using extend().
list.index(elem) -- searches for the given element from the start of the list and returns its index. Throws a ValueError if the element does not appear (use "in" to check without a ValueError).
list.remove(elem) -- searches for the first instance of the given element and removes it (throws ValueError if not present)
list.sort() -- sorts the list in place (does not return it). (The sorted() function shown later is preferred.)
list.reverse() -- reverses the list in place (does not return it)
list.pop(index) -- removes and returns the element at the given index. Returns the rightmost element if index is omitted (roughly the opposite of append()).
"""

list = ['larry', 'curly', 'moe']
list.append('shemp')         ## append elem at end
list.insert(0, 'xxx')        ## insert elem at index 0
list.extend(['yyy', 'zzz'])  ## add list of elems at end
print(list)  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']
print(list.index('curly'))    ## 2

list.remove('curly')         ## search and remove that element
list.pop(1)                  ## removes and returns 'larry'
print(list)  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']

list = [1, 2, 3]
print(list.append(4))   ## NO, does not work, append() returns None
## Correct pattern:
list.append(4)
print(list)  ## [1, 2, 3, 4]


list = []          ## Start as the empty list
list.append('a')   ## Use append() to add elements
list.append('b')


list = ['a', 'b', 'c', 'd']
print(list[1:-1])   ## ['b', 'c']
list[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
print(list)         ## ['z', 'c', 'd']


a = [5, 1, 4, 3]
print(sorted(a))  ## [1, 3, 4, 5]
print(a)  ## [5, 1, 4, 3]

strs = ['aa', 'BB', 'zz', 'CC']
print(sorted(strs))  ## ['BB', 'CC', 'aa', 'zz'] (case sensitive)
print(sorted(strs, reverse=True))   ## ['zz', 'aa', 'CC', 'BB'] optional rreveerse

strs = ['ccc', 'aaaa', 'd', 'bb'] ## can sort by 
print(sorted(strs, key=len))  ## ['d', 'bb', 'ccc', 'aaaa']

# "key" argument specifying str.lower function to use for sorting
print(sorted(strs, key=str.lower))  ## ['aa', 'BB', 'CC', 'zz']

### sorting with own function 
## Say we have a list of strings we want to sort by the last letter of the string.
strs = ['xc', 'zb', 'yd' ,'wa']

## Write a little function that takes a string, and returns its last letter.
## This will be the key function (takes in 1 value, returns 1 value).
def MyFn(s):
  return s[-1]

## Now pass key=MyFn to sorted() to sort by the last letter:
print(sorted(strs, key=MyFn))  ## ['wa', 'zb', 'xc', 'yd']

from operator import itemgetter

# (first name, last name, score) tuples
grade = [('Freddy', 'Frank', 3), ('Anil', 'Frank', 100), ('Anil', 'Wang', 24)]
sorted(grade, key=itemgetter(1,0))
# [('Anil', 'Frank', 100), ('Freddy', 'Frank', 3), ('Anil', 'Wang', 24)]

sorted(grade, key=itemgetter(0,-1))
#[('Anil', 'Wang', 24), ('Anil', 'Frank', 100), ('Freddy', 'Frank', 3)]

#Tuples
tuple = (1, 2, 'hi')
print(len(tuple))  ## 3
print(tuple[2])    ## hi
#tuple[2] = 'bye'  ## NO, tuples cannot be changed
tuple = (1, 2, 'bye')  ## this works

tuple = ('hi',)   ## size-1 tuple

print('--------------')
(x, y, z) = (42, 13, "hike")
print(z)  ## hike

#  List Comprehensions 
nums = [1, 2, 3, 4]
squares = [ n * n for n in nums ]   ## [1, 4, 9, 16]

strs = ['hello', 'and', 'goodbye']

shouting = [ s.upper() + '!!!' for s in strs ]
## ['HELLO!!!', 'AND!!!', 'GOODBYE!!!']

## Select values <= 2
nums = [2, 8, 1, 6]
small = [ n for n in nums if n <= 2 ]  ## [2, 1]

## Select fruits containing 'a', change to upper case
fruits = ['apple', 'cherry', 'banana', 'lemon']
afruits = [ s.upper() for s in fruits if 'a' in s ]
## ['APPLE', 'BANANA']













