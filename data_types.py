
'''
This code provides examples of python data types.
'''


#█████████████████████████████████████████████████████████████████████████████
#█████ Data Types ████████████████████████████████████████████████████████████
#█████████████████████████████████████████████████████████████████████████████

# Strings
'I am string!'
"I've got an apostrophe"
len('Stringie')
'Rootie Tootie' + ' On Youtie'
'Rootie Tootie' * 3
'Rootie Tootie'[3]
'Rootie Tootie'[-2]
'Rootie Tootie'[4:]
'Rootie Tootie'[-5:]
'tie' in 'Rootie Tootie'
'tie' not in 'Rootie Tootie'
'''This is a
multiline string!'''
'I am {} and my name {}'.format(27, 'Robert')
'I will reference {var1} and {var2} again. {var1}{var2}'.format(var1='YIPPIE', var2='!')
'I think, therefore, I yam.'.split()
'I think, therefore, I yam.'.split(sep=',')
str(5)
str({2, 4, 6, 8})

# Booleans
True
False

# Numerics - Integers, Floats, & Complex Numbers
type(4)
type(4.5)
type(4+4j)
isinstance(4, int)
isinstance(4.5, float)
isinstance(4+4j, complex)
float(2)
int(2.6)

# Math
11 + 2
11 - 2
11 * 2
11 / 2

114 % 10
114 // 10

11 ** 2

# Fractions
import fractions
fractions.Fraction(1, 3)
fractions.Fraction(1, 4) * fractions.Fraction(2, 3)

# Trigonometry
import math
math.pi
math.sin(math.pi / 2)
math.cos(0)
math.tan(math.pi / 4)


# Sets
set_numbers = {2, 5}
type(set_numbers)
len(set_numbers)
set_numbers.add(1)
set_numbers
5 in set_numbers
set_numbers.update({3, 4})
set_numbers.update({6, 7}, {8, 9})
set_numbers.update([10, 11])
set_numbers.discard(2)
set_numbers.discard(2)  # Discard does not return an error.
set_numbers.remove(3)
set_numbers.remove(3)  # Remove returns an error.
set_numbers.clear()
# Combining & Joining Sets
set_a = set(range(7))
set_b = set(list(range(11))[4:])
set_a
set_b
set_a.union(set_b)
set_a.intersection(set_b)
set_a.difference(set_b)
set_a.symmetric_difference(set_b)
# Checking Supersets & Subsets
set_a.union(set_b).issuperset(set_a)
set_a.intersection(set_b).issubset(set_b)

# None
if None:
    print("Yes")
elif not None:
    print("No")
