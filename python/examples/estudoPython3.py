#!/usr/bin/env python3

from array import array

# COLLECTIONS

### Arrays --> Objects in Python / Must all be the same type / Numerical data types
scores = array('d')
scores.append(97)
print("The array items are: " + str(scores))

### Lists [] - Stores any data type / Mutable
names = ['Christopher','Susan','Michael','Katherine']
grades = []
grades.append(float(10)) ; print(grades)
print(grades[0])

print(len(grades)) #> Return length of a list
print(names.insert(0, 'Bill')) #> Insert before index
print(names[1:3])

### Dictionaries --- Key value pairs / Storage order not guaranteed

person_age = {'mike':'32','katherine':'28'}
print(person_age)

name_to_find = "Katherine"
key = False

if name_to_find.lower() in person_age:
    key = True
else:
    key = False

if key:
    print(name_to_find + " is here")
else:
    print(name_to_find + " is not here")

#> Dictionaries allow for the creation of object-like types within lists
members = [{'name':'susana','age':'32'},{'name':'mike','age':'24'},{'name':'charles','age':'65'},{'name':'jim','age':'27'}]
print(members[0].get('age')) #> Printing specific field from field 0 --> order not guaranteed. So the result might change.

print(list(filter(lambda usertofind: usertofind['name'] ==  'susana', members)))

