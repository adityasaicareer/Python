type("aditya sai")
print(type("aditya sai"))

# escape sequence

print('aditya\'s sai')
print("I'm Adithya")
print("\"Hello I\'m Aditya\"")

example='Hey you'

for i in range(0,len(example)):
    print(example[i])

print("    "+example[4])
print(example[:])
print(example[3:])

# to reverse a string
print(example[::-1])

# to print alternative charecters
print(example[::2])

# concantination of the strings
print("aditya"+" "+"sai")
print('*'*10)

# lets constrict a pyramid

for i in range(1,11,1):
    print(i*'*')

# string functions 

# len is an function which will give the length of the strings
print(len(example))

# strip will remove all the whitespaces in start and end
print("  i am aditya   ".strip())

# to remove specific charecters on both sides
print("hello".strip('o'))

# to split a sentence to words default whitespace
print("hello i am aditya".split())

#startswith
print(example.startswith("Hey"))
print(example.startswith("hey"))

# endswith
print(example.endswith("you"))
print(example.endswith("You"))

# to find the index

print(example.index('y'))


print(example)
# to convert to the upper case
print(example.upper())

# to convert to the lower case
print(example.lower())

# to capitalize

print('hi i am aditya'.capitalize())

# find()
print(example.find('Hey'))
print(example.find('you'))

# count

print(example.count('y'))





# string formatting

a=10
b=5
print(f"this is a formatted string {a+b},{a-b},{a*b}")
print("this is a formatted string {},{},{}".format(a+b,a-b,a*b))
print("this is a format stirng %d %d %d"%(a+b,a-b,a*b))