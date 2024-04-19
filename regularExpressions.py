#Regular expressions

#The Python "re" module provides regular expression support.
import re

#The re.search() method takes a regular expression pattern and a string and searches for
#that pattern within the string. 

str = 'an example word:cat!!'
#The 'r' at the start of the pattern string designates a python "raw" string which passes through 
#backslashes without change which is very handy for regular expressions (Java needs this feature badly!). 
#I recommend that you always write pattern strings with the 'r' just as a habit.
match = re.search(r'word:\w\w\w', str)
# If-statement after search() tests if it succeeded
if match:
  print('found', match.group()) ## 'found word:cat'
else:
  print('did not find')


# RULES

#The search proceeds through the string from start to end, stopping at the first match found
#All of the pattern must be matched, but not all of the string
#If match = re.search(pat, str) is successful, match is not None and in particular match.group() is the matching text

## Search for pattern 'iii' in string 'piiig'.
## All of the pattern must match, but it may appear anywhere.
## On success, match.group() is matched text.
match = re.search(r'iii', 'piiig') # found, match.group() == "iii"
match = re.search(r'igs', 'piiig') # not found, match == None

## . = any char but \n
match = re.search(r'..g', 'piiig') # found, match.group() == "iig"

## \d = digit char, \w = word char
match = re.search(r'\d\d\d', 'p123g') # found, match.group() == "123"
match = re.search(r'\w\w\w', '@@abcd!!') # found, match.group() == "abc"


# + -- 1 or more occurrences of the pattern to its left, e.g. 'i+' = one or more i's
# * -- 0 or more occurrences of the pattern to its left
# ? -- match 0 or 1 occurrences of the pattern to its left



#repetition

## i+ = one or more i's, as many as possible.
match = re.search(r'pi+', 'piiig') # found, match.group() == "piii"

## Finds the first/leftmost solution, and within it drives the +
## as far as possible (aka 'leftmost and largest').
## In this example, note that it does not get to the second set of i's.
match = re.search(r'i+', 'piigiiii') # found, match.group() == "ii"

## \s* = zero or more whitespace chars
## Here look for 3 digits, possibly separated by whitespace.
match = re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx') # found, match.group() == "1 2   3"
match = re.search(r'\d\s*\d\s*\d', 'xx12  3xx') # found, match.group() == "12  3"
match = re.search(r'\d\s*\d\s*\d', 'xx123xx') # found, match.group() == "123"

## ^ = matches the start of string, so this fails:
match = re.search(r'^b\w+', 'foobar') # not found, match == None
## but without the ^ it succeeds:
match = re.search(r'b\w+', 'foobar') # found, match.group() == "bar"

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'[\w.-]+@[\w.-]+', str)
if match:
  print(match.group())  ## 'alice-b@google.com'
# Square brackets can be used to indicate a set of chars, so [abc] matches 'a' or 'b' or 'c'. The codes \w, \s etc. work inside square brackets too with the one exception that dot (.) just means a literal dot. 
# An up-hat (^) at the start of a square-bracket set inverts it, so [^ab] means any char except 'a' or 'b'.

#findall()
#findall() finds *all* the matches and returns them as a list of strings, with each string representing one match.



#group extraction
#In this case, the parentheses do not change what the pattern will match, instead they establish logical "groups" inside of the match text.
str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'([\w.-]+)@([\w.-]+)', str)
if match:
  print(match.group())   ## 'alice-b@google.com' (the whole match)
  print(match.group(1))  ## 'alice-b' (the username, group 1)
  print(match.group(2))  ## 'google.com' (the host, group 2)
  
## Suppose we have a text with many email addresses
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'

## Here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str) ## ['alice@google.com', 'bob@abc.com']
for email in emails:
  # do something with each found email string
  print(email)
 

# Open file. for files findall do de iteration
f = open('foo.txt', encoding='utf-8')
# Feed the file text into findall(); it returns a list of all the found strings
strings = re.findall(r'some pattern', f.read())

#findall and Groups
#If the pattern includes 2 or more parentheses groups, then instead of returning a list of strings, findall()
str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
print(tuples)  ## [('alice', 'google.com'), ('bob', 'abc.com')]
for tuple in tuples:
  print(tuple[0])  ## username
  print(tuple[1])  ## host

















