# from Collections import Counter 

marriage=[22,22,25,25,30,24,26,24,35]

x=5
y=6
print(x+y)

# valuecounts=Counter(marriage)
# print(valuecounts)

def add(a,b):
    sum=a+b
    return sum


print(add(1,2))

# there are anonymous functions were also available in python

a=lambda x,y: x+y
print(a(4,5))

power=lambda x,y:x**y

print(power(3,4))

# lists in python useful datastructures represented by [] ordered,changable,allow duplications

p1=[1,2,3,4,5,6,7,8,9]
p2=p1[0:5]
print(p2)
# p2 would be the same if p2 is p1[:5]

# sum of elements in lists

depth=[1,2,3,4,5]
d1=depth[0:3]
print(sum(depth),sum(d1))

print(max(depth))
print(f"the min is {min(depth)}")

print(depth[-1])
print(depth[-2:])
print(5 in depth)
print(7 in depth)

# append method

depth.append(10)
depth.append(11)
print(depth)

depth.extend([100,200])
print(depth)

# append used to add one element and extend used to add multiple elements

# dictionary
# key-pair values

mydict={"age":21,"firstname":'adithya','lastname':'vidivada','siblings':['aditya','amrutha']}
print(mydict)

print(mydict['age'])

print(mydict['firstname'])
print(mydict['lastname'])
print(mydict['siblings'])

# check a key
print('age' in mydict)
print('firstname' in mydict)
print('name' in mydict)
# to get the value of a key

print(mydict.get('age'))
print(mydict.get('firstname'))
# for all the keys
print(mydict.keys())
# for all the values
print(mydict.values())
print('\n\n')
print(mydict.items())

# sets in python
# sets is an unordered collection of unique elements any duplications were removed automatically
print('\n\n')
myset=set()
myset.add(1)
myset.add(2)
myset.add(3)
print(myset)
myset.add(1)
print(myset)
myset.add(4)

myset1=set()
myset1.add(1)
myset1.add(2)
myset1.add(3)
myset1.add(4)
myset1.add(5)

print(myset.intersection(myset1))
print(myset.union(myset1))

# to find the difference

print(myset.difference(myset1))
print(myset1.difference(myset))

# built-in functions and control flow in python
# function to check the age

def checkage(age):
    if(age>=40):
        print("you are older than 40 ")
    elif(age<40 and age>30):
        print("your age is between 30 and 40")
    else:
        print("your age is below 30")
    return

print(checkage(34))
print(checkage(45))

# the for construct

names=['srinivasarao','rajyalakshmi','aditya','amruth']

for i,name in enumerate(names):

    print(f"the index {i} and value is {name}")

# listcomprehensions means construction of list based on existing lists

lis=[1,2,3,4,5,6]
newlis=[x for x in lis if x%2==0]
print(newlis)

firstl=[x for x in range(1,10,1)]
print(firstl)

five=[i+1 for i in range(5)]
print(five)

# built in functions 
# sort
mylist=[4,3,5,1,5]
mylist.sort()
print(mylist)

# we can also use the sorted function for more and more control over the sorting
slist=[4,5,2,5,9,2]
slist_s=sorted(slist,reverse=True)
print(slist_s)

# zip function
l1=[1,2,3]
l2=['a','b','c']

print(zip(l1,l2))
# zip will give the tuples
listed=list(zip(l1,l2))
print(listed)

# and we can break into two tuples
num,alpha=zip(*listed)
print(num,alpha)

# numpy as external library
