l=[1,2,'3',True]

# we can store the multiple datatypes in python

print(type(l))
print(l)
print(len(l))

print(l.index(1))
print(l.count(2))

print(l[2:3])
print(l[::-1])
print(l.reverse())
print(l*2)
print(l+[100,101,102])

# to apend the elements at the end

l.append(1000)
print(l)

l.extend([11,12,13])
print(l)


l.insert(2,'aditya')
print(l)


print(''.join(['aditya','sai']))

newlist=l.copy()

print(newlist)


# remove elements from the list

print(l.pop())
print(l.remove(2))
print(l)

nums=[5,4,3,6,7,1]
print(nums.sort())

print(nums)

## in descending order

print(nums.sort(reverse=True))
print(nums)

print(1 in l)
print(max(nums))
print(min(nums))

## to break the list

sam=[i for i in range(100)]

first,*x,last=sam
print(first,x,last)


# martix

mat=[[1,2,3],[4,5,6],[7,8,9]]
print(mat)

for i in mat:
	for j in i:
		print(j,end=" ")

print()

a=[i for i in 'hello']
print(a)

s2=[i for i in range(1,100) if i%2==0]
print(s2)

## sunfunctions


print(sum(s2))
pairs=[p for p in zip([1,2,3],[4,5,6])]

print(pairs)
print(type(pairs[0]))


# the above p gives us the tuple


