dic={'name':'Aditya','age':25,'magic_power':False}
print(dic)

## retirival

print(dic['name'])

print(len(dic))
print(list(dic))
print(dic.keys())
print(dic.values())

print(dic.items())

dic['weight']=90

print(dic)
## get method

print(dic.get('name'))
del dic['magic_power']
print(dic)

dic.update({'name':"Aditya Sai"})
print(dic)

newdict=dict(zip(['name','age'],['aditya',20]))
print(newdict)


for k,v in dic.items():
	print(k)
	print(v)
