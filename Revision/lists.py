mylist=[1,2,'3',True,4,5,4,6,4,7]
# we can add any type of data in an linkedlist
print(type(mylist))

#length of the list

print(len(mylist))

# to get the index of the list

print(mylist.index('3'))

# to count the a particular value

print(mylist.count(4))

print(mylist[3])
print(mylist[1:])
print(mylist[2:6])

# to reverse a list

print(mylist[::-1])

# to print the list alternate elements

print(mylist[::2])

print(mylist*2)
# my multiplication the list all the elements of the list wiill be repeated 

# adding at the end

mylist.append(100)
print(mylist)

l=['*']
for i in range(1,10,1):
    print(l*i)

mylist.extend([100,200,300])
print(mylist)
# extend method will add multiple values at a time to the list

# to insert an element at an index

mylist.insert(2,1000)
print(mylist)

# we can join all the elements of the list into the string

greet=["hi","there","how","are","you"]
print(" ".join(greet))

# lets print the pyramid again

for i in range(1,10,1):
    print(" ".join(l*i))

# copy a list

# copying a list is very dfficult taks as all the lists were stored in the form of the address

# if we directly assign to another they would point to the same memory locations

basket=['apples','bananas','watermelon']
newbasket=basket.copy()
newbasket1=basket[:]
newbasket.append(1000)
print(newbasket,basket)

# removing from the list

list=[i for i in range(1,10,1)]
print(list)

print(list.pop(),list)
# to remove the particular element at an index

list.pop(2)
print(list)

# to remove a particular number

list.remove(5)

print(list)

# to reverse a list
list.reverse()
print(list)

# to clear the list
list.clear()
print(list)
# to sort the list

unsorted=[5,3,7,2,7]
sort=sorted(unsorted)
print(sort)

# in descending order

des=sorted(unsorted,reverse=True)
print(des)

print( 3 in des)
print(max(des))
print(min(des))
print(sum(des))

# get the first and last of the list
list=[i**2 for i in range(5)]
print(list)

first,*x,last=list
print(first,last)