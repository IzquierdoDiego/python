print('         ')
print('------------------')
print('******************')
print('         ')



#def keyword defines the function with its parameters within parentheses and its code indented. 
def repeat(s, exclaim):
  """
  Returns the string 's' repeated 3 times.
  If exclaim is true, add exclamation marks.
  """

  result = s + s + s # can also use "s * 3" which is faster (Why?)
  #Both + and * are called "overloaded" operators because they mean different things for numbers vs. for strings (and other data types).
  if exclaim:
    result = result + '!!!'
  return result
    
def main():
  print(repeat('Yay', False))      ## YayYayYay
  print(repeat('Woo Hoo', True))   ## Woo HooWoo HooWoo Hoo!!!
  
  s = 'hi'
  print(s[1])          ## i  Characters in a string can be accessed using the standard [ ] syntax
  print(len(s))					## 2
  print(s + ' there')  ## hi there
  pi = 3.14
  #text = 'The value of pi is ' + pi      ## NO, does not work
  text = 'The value of pi is '  + str(pi)  ## yes
  
  raw = r'this\t\n and that'

  # this\t\n and that
  print(raw)
  
  multi = """It was the best of times.
  It was the worst of times."""

  # It was the best of times.
  #   It was the worst of times.
  print(multi)
 
  value = 2.791514
  print(f'approximate value = {value:.2f}')  # approximate value = 2.79
  print(value)

  car = {'tires':4, 'doors':2}
  print(f'car = {car}') # car = {'tires': 4, 'doors': 2}

  print('\n')
  address_book = [{'name':'N.X.', 'addr':'15 Jones St', 'bonus': 70},
  	{'name':'J.P.', 'addr':'1005 5th St', 'bonus': 400},
  	{'name':'A.A.', 'addr':'200001 Bdwy', 'bonus': 5},]

  for person in address_book:
    print(f'{person["name"]:8} || {person["addr"]:20} || {person["bonus"]:>5}')
  
#Python prefers the underscore method nombre_variable_con_guion
if __name__ == '__main__':
	main()
	print('         ')
	print('******************')
	print('------------------')
	print('         ')
