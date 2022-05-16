# 1
names = ['John', 'Sue', 'Bob', 'Chris']
for i in range(len(names)):
    print(names[i])

# New:
for name in names:
    print(name)

# 2-3

# 4
names2 = ['Rens', 'Foppe', 'Theo', "Theo's moeder"]

for i in range(len(names)):
    print(f'{names[i]}, {names2[i]}')

# 5
list(zip(names, names2))

# 6

# 7
# Only the elements with the lowest list range are paired

# type(zip) is <class 'zip'> which is an iterator-object. So the object itself does not give anything, it's only when you iterate over it that it can give you something

# 8

# 9
zipnames = list(zip(names, names2))
# [('John', 'Rens'), ('Sue', 'Foppe'), ('Bob', 'Theo'), ('Chris', "Theo's moeder")]
zipnames = dict(zip(names, names2))
# {'John': 'Rens', 'Sue': 'Foppe', 'Bob': 'Theo', 'Chris': "Theo's moeder"}
zipnames = tuple(zip(names, names2))
# (('John', 'Rens'), ('Sue', 'Foppe'), ('Bob', 'Theo'), ('Chris', "Theo's moeder"))

# int, str don't work

# 10
names3 = ['Joseph', 'Michal']
print(list(zip(names, names2, names3)))
# [('John', 'Rens', 'Joseph'), ('Sue', 'Foppe', 'Michal')]

# 11
placenames = ['Amsterdam', 'Hillegom', 'Lidda']
inhabitant_counts = ['184905', '243', '09876543']
print(dict(zip(placenames, inhabitant_counts)))
# {'Amsterdam': '184905', 'Hillegom': '243', 'Lidda': '09876543'}

# 12-13
# all fine, these are different ways to combine them

# 14
print(list(zip(s[0:6:2], s[1:6:2])))
# [('a', 'b'), ('c', 'd'), ('e', 'f')]

# 15
# No
# result: for every element, append the two lists together to the result
# zip: zip them together

# 16
# 0 John
# 1 Sue
# 2 Bob
# 3 Chris

# 17
for name in enumerate(names):
    print(i, name)
# 3(0, 'John')
# 3(1, 'Sue')
# 3(2, 'Bob')
# 3(3, 'Chris')
# it prints a (random?) index and then every element in enumerate(names), which are just tuples of the indices with their corresponding elements

for i, name in names:
    print(i, name)
# error

# 18
# idk

# 19

# enumerate
# lists, tuples:
for i, char in enumerate(names):
    print(i, char)
# 0 John
# 1 Sue
# 2 Bob
# 3 Chris

# dictionaries
dic1 = {'huh': 'oh!', 'cool': 'ikke'}
for i, char in enumerate(dic1.keys()):
    print(i, char)
# 0 huh
# 1 cool
# dic1.keys = dic1

for i, char in enumerate(dic1.values()):
    print(i, char)
# 0 oh!
# 1 ikke

for i, char in enumerate(dic1.items()):
    print(i, char)
# 0 ('huh', 'oh!')
# 1 ('cool', 'ikke')

# strings also work
# int does not

# 19-21

# 22-23

# 24
words = ['The', 'quick', 'brown', 'fox', 'jumped', 'over', 'the', 'turtle']

all(len(word) < 10 for word in words)
# True
any(word[0] in 'aeiou' for word in words)
# True

# 25
all(not 't' in word.lower() for word in words)
any('t' in word.lower() for word in words)
all('t' in word.lower() for word in words)

# 26
list1 = [1, 2, 3, 4, 5]
list2 = ['abc', 'def']
list3 = [True, True, False]

sum(list1)
# 15, counts ints in the list
sum(list2)
# error
sum(list3)
# 2, counts number of True bools

list4 = [[1, 2, 3, 4, 5], ['abc', 'def'], [True, True, False]]
list5 = [(1, 2), (3, 4), (5, 6)]
list6 = [{1: 'een'}, {2: 'twee'}, {3: 'drie'}]

# all these sum() give an error (cannot + int and list, int and tuple, int and dict, and also not int and string.
# it seemingly only counts numbers: either an int, or a boolean True, probably underlyingly corresponding to 1

# 27
sum(len(word) >= 3 for word in words)
# 8
sum([word[-1] in 'aeiou' for word in words]) >= 3
# True

# 28
len([word for word in words if word[-1] in 'aeiou']) >= 3
# True

# 29
any(w[0].lower() in 'aeiou' for w in words)
# some words start with a vowel

all(w[0].lower() in 'aeiou' for w in words)
# all words start with a vowel

not any(w[0].lower() in 'aeiou' for w in words)
# no words start with a vowel

all(w[0].lower() not in 'aeiou' for w in words)
# no word starts with a vowel

sum(w[0].lower() in 'aeiou' for w in words) >= 2
# the amount of words that start with a vowel is 2 or higher

len([w for w in words if w[0].lower() in 'aeiou']) >= 2
# the amount of words that start with a vowel is 2 or higher

not any(w[0].lower() not in 'aeiou' for w in words)
# no word starts with a consonant

# 32
# haha nee