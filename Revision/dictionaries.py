mydict={'name':'Aditya sai','age':22,'magic-power':False}

print(mydict)
print(mydict['name'])
print(mydict['age'])

# length of the dictionaries

print(len(mydict))

# to find the keys of the dictionaries
print(mydict.keys())

# to print the all the values of the dictionaries

print(mydict.values())

# now convert the dict.keys and dict.values to the lists

keys=list(mydict.keys())
values=list(mydict.values())

print(keys,values)

# to make the modifications

mydict['magic_power']="i guess sometimes"

print(mydict)

# to get the value using the .get method

print(mydict.get('age'))

# to remove a key

del mydict['magic_power']
print(mydict)

mydict.pop('name')
print(mydict)

mydict.update({'age':21})
print(mydict)

mydict['name']='Aditya Sai'
print(mydict)

newdict=dict([['name','aditya'],['age',22]])
print(newdict)

dict2={key:value for key,value in newdict.items()}
print(dict2)