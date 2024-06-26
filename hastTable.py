# Dict Hash Table

## Can build up a dict by starting with the empty dict {}
## and storing key/value pairs into the dict like this:
## dict[key] = value-for-that-key
dict = {}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'

print(dict) ## {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

print(dict['a'])     ## Simple lookup, returns 'alpha'
dict['a'] = 6       ## Put new key/value into dict
'a' in dict         ## True
## print(dict['z'])                  ## Throws KeyError
if 'z' in dict: print(dict['z'])     ## Avoid KeyError
print(dict.get('z'))  ## None (instead of KeyError)

## By default, iterating over a dict iterates over its keys.
## Note that the keys are in a random order.
for key in dict:
  print(key)
## prints a g o

## Exactly the same as above
for key in dict.keys():
  print(key)

## Get the .keys() list:
print(dict.keys())  ## dict_keys(['a', 'o', 'g'])

## Likewise, there's a .values() list of values
print(dict.values())  ## dict_values(['alpha', 'omega', 'gamma'])

## Common case -- loop over the keys in sorted order,
## accessing each key/value
for key in sorted(dict.keys()):
  print(key, dict[key])

## .items() is the dict expressed as (key, value) tuples
print(dict.items())  ##  dict_items([('a', 'alpha'), ('o', 'omega'), ('g', 'gamma')])

## This loop syntax accesses the whole dict by looping
## over the .items() tuple list, accessing one (key, value)
## pair on each iteration.
for k, v in dict.items(): print(k, '>', v)
## a > alpha    o > omega     g > gamma

print()
h = {}
h['word'] = 'garfield'
h['count'] = 42
s = 'I want %(count)d copies of %(word)s' % h  # %d for int, %s for string
# 'I want 42 copies of garfield'

# You can also use str.format().
s = 'I want {count:d} copies of {word}'.format(**h)
print(s)
print()

#del, deleting
var = 6
del var  # var no more!

list = ['a', 'b', 'c', 'd']
del list[0]     ## Delete first element
del list[-2:]   ## Delete last two elements
print(list)      ## ['b']

dict = {'a':1, 'b':2, 'c':3}
del dict['b']   ## Delete 'b' entry
print(dict)      ## {'a':1, 'c':3}

# Echo the contents of a text file
f = open('foo.txt', 'rt', encoding='utf-8')
for line in f:   ## iterates over the lines of the file
  print(line, end='')    ## end='' so print does not add an end-of-line char
                         ## since 'line' already includes the end-of-line.
f.close()

f = open('foo.txt', 'wt', encoding='utf-8')
f.write('linea creada desde python') ## end='' so print does not add an end-of-line char
                         ## since 'line' already includes the end-of-line.
f.write('second line from python')
"print(string, file=f)"
f.close()







