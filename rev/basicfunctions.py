print(len('aditya'))
print(len([1,2,3,4]))


# to remove the all the white spaces in the strings

ex='  aditya   '

print(ex.strip())

print(ex.strip('a'))

ex2='aditya'
print(ex2.strip('a'))

# split the sentences

complete='vidivada chowdary adithya sai'

l=complete.split(" ")
print(l)

# replace function

print(complete.replace('a','z'))

# to find the charecter

print(complete.find('a'))
# to get the first index

print(complete.index('a'))

print(complete.capitalize())

print(complete.count('a'))


## stirng formatting

name1='aditya'
name2='sai'

print(f"my first name is {name1} and last name is {name2}")

print('hrllo my name is {} and {}'.format(name1,name2))




