#!/usr/bin/env python

#Sets (unordered collection of unique objects)

s = 'django'

print(s[0])
print(s[-1])
print(s[:4])
print(s[1:4])
print(s[-2:])

d1 = {'simple_key':'hello'}
d2 = {'k1':{'k2':'hello'}}
d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print(d1['simple_key'])
print(d2['k1']['k2'])

mylist = [1,1,1,1,1,1,2,2,2,2,2,3,3,3,3]

#print({mylist})

age = 4
name = "sammy"

print(f"Hello my dog's name is {name} and he is {age} years old")
print("Hello, my dog's name is {name} and he is {age} years old".format(age=age,name=name))

#comparison and logical operators

a = 7
b = 7

if a > b:
    if a > 10:
        print("a is bigger than b and 10")
    else:
        print("a is bigger than b but not bigger than 10")
elif b > a:
    print("a is not bigger than b")
else:
    print("they are equal")

#for loops

seq = [1,2,3,4,5,6]

for item in seq:
    print(item)

d = {"Sam":1,"Frank":2,"Dan":3}

for item in d:
    print(item)

mylist = [(1,2),(3,4),(5,6)]

for (tup1,tup2) in mylist:
    print(tup1)
    print(tup2)

i = 1

while i<5:
    print("i is equal to {}".format(i))
    i+=1

for item in range(1,11):
    print(item)

def somaNumeros(n1=0,n2=0):
    """
    This function takes two numbers as arguments and returns the sum of both
    """
    return n1+n2


print(somaNumeros(6,5))     
