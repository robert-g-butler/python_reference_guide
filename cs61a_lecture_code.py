
'''
This code follows the reading material from the Berkeley class CS61A.

Reading material can be found here:
https://inst.eecs.berkeley.edu/~cs61a/fa16/
'''


#█████ 1.2 - Elements of Programming █████████████████████████████████████████

# Importing Functions from Modules
from urllib.request import urlopen
from operator import mul, add, sub
from math import pi, sqrt, exp

#█████ 1.4 - Designing Functions █████████████████████████████████████████████

# Create user-defined fuctions
def pressure(v, t, n = 6.022e23):
    '''Compute the pressure in pascals of an ideal gas.
    
    Applies the ideal gas law: http://en.wikipedia.org/wiki/Ideal_gas_law
    
    v -- volume of gas, in cubic meters
    t -- absolute temperature in degrees kelvin
    n -- particles of gas
    '''
    k = 1.38e-23  # Boltzmann's constant
    return n * k * t / v
help(pressure)
pressure(1, 273.15)

# Assign variables
var1 = 5
var2, var3 = 10, 15
var1
var2
var3

# Print to console
print('Hello world')

#█████ 1.5 - Control █████████████████████████████████████████████████████████

# Conditional Statements
def func_abs_value(x):
    '''Return the absolute value of x.'''
    if x < 0:
        return -x
    elif x == 0:
        return 0
    else:
        return x

func_abs_value(-5)

# Iteration - While statements
def func_fib(n):
    '''Calculates the nth Fibonacci number.'''
    curr_num, prev_num = 1, 0
    i = 1
    while i < n:
        print('Fibonacci Number', i, 'is:', curr_num)
        prev_num, curr_num = curr_num, curr_num + prev_num
        i = i + 1
    return curr_num

func_fib(8)

# Assert Testing - Use assertions to verify if variables are input as expected.
def func_checkinput(x):
    assert x > 0, 'Please provide a positive input number.'
    return func_fib(x)
func_checkinput(-12)

#█████ 1.6 - Higher-Order Functions ██████████████████████████████████████████

# Higher Order Functions - Use higher-order functions to manipulate functions with a function
def summation(n, func):
    '''Sums func(1) to func(n).'''
    i, total = 1, 0
    while i <= n:
        print('At', i, ', we do:', round(total, 2), '+', round(func(i), 2))
        i, total = i + 1, total + func(i)
    return total

summation(10, sqrt)

def cube(x):
    return x * x * x
summation(10, cube)

# Higher Order Functions - Chain functions together to find the golden ratio.
def func_iterative_loop(improve_function, close_function, guess = 1):
    while not close_function(guess):
        print(guess)
        guess = improve_function(guess)
    return guess
def func_golden_ratio_iteration_formula(x):
    return 1 / x + 1
def func_golden_ratio_tolerance_check(x, tolerance = 1e-10):
    return abs( (x * x) - (x + 1) ) < tolerance

func_iterative_loop(improve_function = func_golden_ratio_iteration_formula,
                    close_function = func_golden_ratio_tolerance_check)

# Nested Definitons -  Do a similar nest for finding sqrt, and nest all functions in one.
def func_sqrt(arg1):    
    def func_iterative_loop(improve_function, close_function, guess = 1):
        while not close_function(guess):
            print(guess)
            guess = improve_function(guess)
        return guess
    def func_sqrt_iteration_formula(x):
        '''This function returns the average of arg1 and the guess.'''
        return (x + (arg1 / x)) / 2
    def func_sqrt_tolerance_check(x, tolerance = 1e-10):
        return abs( (x * x) - (arg1) ) < tolerance
    return func_iterative_loop(improve_function = func_sqrt_iteration_formula,
                               close_function = func_sqrt_tolerance_check)
func_sqrt(256)

# Lambda Expressions - Assign a function with lambda instead of def.
func_cube = lambda x: x * x * x
func_cube(3)

# Map
from math import sqrt
mapped_expression = map(sqrt, list(range(15)))
mapped_expression
list(mapped_expression)

list(map(lambda x: x*x, list(range(11))))

# Function Decorators - Use @ to add a function 'trace' to another function's definition. Do so without '@', as well.
def func_trace(fn):
    def func_wrapper(x):
        print('-->', fn, '(', x, ')')
        return fn(x)
    return func_wrapper

@func_trace
def func_x3(x):
    return x * 3
func_x3(3)

def func_x3(x):
    return x * 3
func_x3(3)
func_trace(func_x3)(3)

#█████ 1.7 - Recursive Functions █████████████████████████████████████████████

# Recursion - sum the digits of numbers.
def func_sum_digits(x):
    def func_split(x):
        return x // 10, x % 10
    if x < 10:
        return x
    else:
        dbl_10s_digits, dbl_1s_digit = func_split(x)
        return func_sum_digits(dbl_10s_digits) + dbl_1s_digit
func_sum_digits(8453)

from math import pi
func_sum_digits(pi*1e100)

# Tree Recursion
def func_fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return func_fibonacci(x - 2) + func_fibonacci(x - 1)
func_fibonacci(30)

# Tree Recursion - this one's too confusing for me. Draw a tree diagram to follow the execution.
def func_count_partitions(x, y):
    '''Count the number of ways to partition (sum) x, using numbers up to y.'''
    if x == 0:
        print('Found one! (', x, ',', y, ')')
        return 1
    elif x < 0:
        print('Stop       (', x, ',', y, ')')
        return 0
    elif y == 0:
        print('Stop       (', x, ',', y, ')')
        return 0
    else:
        print('Next       (', x, ',', y, ')')
        return func_count_partitions(x-y, y) + func_count_partitions(x, y - 1)
func_count_partitions(6, 4)

#█████ 2.3 - Sequences ███████████████████████████████████████████████████████

# Sequence Iteration - For Loop
for x in [0, 1, 2, 3, 4, 5]:
    print(x * 10)

# Sequence Unpacking - For Loop with multiple assignments
for x, y in [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]:
    print('{} x {} = {}'.format(x, y, x*y))

# Ranges
range(1, 5)
list(range(1, 5))
list(range(3))

# For loop with unused variable ( it's standard convention to use _ )
for _ in range(4):
    print('I will say this 4 times!')

# Sequence Processing
odds = [1, 3, 5, 7, 9]
[x+1 for x in odds]
[x for x in odds if 25%x==0]

# Aggregation
odds = [1, 3, 5, 7, 9]
min(odds)
max(odds)
sum(odds)

# Membership
5 in [2, 4, 6, 8, 10]
5 not in [2, 4, 6, 8, 10]

#█████ 2.4 - Mutable Data ████████████████████████████████████████████████████

# Sharing and Identity
list1 = list(range(5))
list2 = list1
list1
list2

list2.pop()  # Affects both lists
list1
list2

list1 is list2
list1 is [0, 1, 2, 3]  # 'is' checks that objects share their identity
list1 == [0, 1, 2, 3]

# Lists (Mutable Sequences) --------------------------------------------------

# Create Lists
list_empty = []
list_empty = list()
list_numbers = [1, 2, 3, 4, 5]
list_numbers
i1, i2, i3, i4, i5 = list_numbers  # Assign multiple variables from list
i1
i2
list( 'ABCDE' )                    # from string
list( {1, 2, 3, 4, 5} )            # from set
list( ('α', 'β', 'γ', 'δ', 'ε') )  # from tuple

# Slice Lists
list_numbers = list(range(10)); list_numbers
list_numbers[0]
list_numbers[1]
list_numbers[-1]
list_numbers[-3]
list_numbers[:3]
list_numbers[3:]
list_numbers[1:-1]
list_numbers[:]

# Add Items to List
list_assorted = list(range(5))
list_assorted + ['text']
list_assorted * 3
list_assorted.append(True); list_assorted
list_assorted.append(['foo', 'foo']); list_assorted
list_assorted.extend(['bar', 'bar']); list_assorted
list_assorted += ['qux', 'qux']; list_assorted  # Same as 'extend'
list_assorted.insert(5, 'λ'); list_assorted

# Remove Items from Lst
list_assorted = list('ABCDE') + list(range(5)); list_assorted
del list_assorted[3:6]; list_assorted
list_assorted.remove(3); list_assorted
list_assorted.pop()  # Last item removed & returned.
list_assorted
list_assorted.pop(-2)
list_assorted

# Get Info from List
list_letters = list('abcde abc cde'); list_letters
len(list_letters)
list_letters.count('c')
list_letters.index('e')
'λ' in list_letters
'e' in list_letters

# Sharing & Identity
#   Assigning nested lists will still link to the original variable name.
list1 = list('abcde'); list1
list2 = list(range(5)); list2
list1.append(list2); list1
list2.pop(2)  # affects both lists b/c list2 is nested in list1s
list1
list2

# Tuples (Immutable Sequences) -----------------------------------------------

# Create Tuples
tuple_empty = tuple()
tuple_empty = ()
tuple_one = ('abcde',)  # Single-element tuples have ',' after 1st item.
(1, 2, 3, 4, 5)
tuple( 'ABCDE' )                    # from string
tuple( [1, 2, 3, 4, 5] )            # from list
tuple( {'α', 'β', 'γ', 'δ', 'ε'} )  # from set

# Slice Tuples
tuple_numbers = tuple(range(10)); tuple_numbers
tuple_numbers[0]
tuple_numbers[1]
tuple_numbers[-1]
tuple_numbers[-3]
tuple_numbers[:3]
tuple_numbers[3:]
tuple_numbers[1:-1]
tuple_numbers[:]

# Add Items to Tuple (Makes a New Tuple)
tuple_numbers = tuple(range(5))
tuple_numbers + ('text',)
tuple_numbers * 3

# Get Info from Tuple
tuple_letters = tuple('abcde abc cde'); tuple_letters
len(tuple_letters)
tuple_letters.count('c')
tuple_letters.index('e')
'λ' in tuple_letters
'e' in tuple_letters

# Multiple Variable Assignment
#   A function can return a tuple to allow multiple return values.
Mon, Tues, Wed, Thur, Fri, Sat, Sun = range(7)
Mon
Fri
(val1, val2, val3) = ('five', 'seven', 'fourty two')
val2

# Dictionaries (Key-Value Pairs) ---------------------------------------------

# Create Dictionaries
{}
{'a': 'A', 'b': 'B', 'c': 'C'}
dict()
dict(one = 1, two = 2, three = 3)
dict(zip(list('abcde'), list(range(5))))

# Iterating To Create Dictionaries (Example 1)
dict_a = {}
for key, value in zip(list('abcde'), list(range(5))): dict_a[key] = value
dict_a

# Iterating To Create Dictionaries (Example 2)
{x: x*x for x in range(1, 10)}

# Get Dictionary Keys & Values
dict_a = {'server': 'db.diveintopython3.org', 'database': 'mysql'}; dict_a
dict_a['server']
dict_a['database']
dict_a.get('database', 'Default Value')
dict_a.get('a', 'Default Value')  # Default is returned if 'a' not found.
    
# Add & Assign Dictionary Items
dict_a = {'server': 'db.diveintopython3.org', 'database': 'mysql'}; dict_a
dict_a['database'] = 'blog'; dict_a
dict_a['user'] = 'John'; dict_a

# Get Info from Dictionary
dict_a = dict(zip(list('abcde'), list(range(5)))); dict_a
len(dict_a)
'a' in dict_a
1 in dict_a
dict_a.keys()
dict_a.values()
dict_a.items()

# Local State ----------------------------------------------------------------

# Make function that that creates new frame with 'balance' and 'func_with...'
def func_make_withdraw(balance = 100):
    def func_withdraw(amount):
        nonlocal balance
        if balance < amount:
            return 'Insufficient funds!'
        else:
            balance = balance - amount
            return balance
    return func_withdraw

#   'balance' is saved in the frame where 'withdraw' is assigned. Python can
#   already reference 'balance' without 'nonlocal', but 'nonlocal' allows it
#   to CHANGE 'balance' outside of the 'func_withdraw' function.

# Use function to make new frame
withdraw = func_make_withdraw(100)
withdraw(15)
withdraw(15)
withdraw(15)

# Iterables & Iterators ------------------------------------------------------

# Iterators are evaluated in a 'lazy' manner, and they only generate values
# when required. This improves performance (speed & memory).

# Create An Iterator with 'iter()' and Iterate Through It with 'next()'
list_numbers = list(range(1, 4))
iter1 = iter(list_numbers)
next(iter1)
next(iter1)
next(iter1)
next(iter1)
type(iter1)

# Assigning an iterator to another will NOT cause nested iterators.
iter1 = iter(list('abcd'))
next(iter1)
iter2 = iter(iter1)
next(iter2)

# A 'for' loop can iterate over contents of a interator.
iter1 = iter(list('abcde'))
next(iter1)
for x in iter1: print(x)

# Built-In Iterator Functions ------------------------------------------------

# Map()
def func1(x): print('** {} --> {} **'.format(x, x*2)); return x*2
rng1 = range(2, 9)
iter_mapped = map(func1, rng1)
next(iter_mapped)
next(iter_mapped)
list(iter_mapped)

# Filter()
func_isnot_vowel = lambda x: x not in list('aeiou')
iter_filtered = filter(func_isnot_vowel, list('abcdefghijklmnopqrstuvwxyz'))
next(iter_filtered)
next(iter_filtered)
list(iter_filtered)

# Zip()
iter_zipped = zip(list('abcde'), list(range(5)))
next(iter_zipped)
next(iter_zipped)
list(iter_zipped)

# Reversed()
iter_reversed = reversed(list('abcde'))
next(iter_reversed)
next(iter_reversed)
list(iter_reversed)

# User-Defined Generators ----------------------------------------------------

def gen_letters():
    current = 'a'
    while current <= 'z':
        yield current
        current = chr(ord(current) + 1)

iter_letters = gen_letters()
next(iter_letters)
next(iter_letters)
list(iter_letters)

# Dispatch Dictionaries ------------------------------------------------------

# The dictionary 'dispatch' is saved within the function below. This is used
# so that we can...
#    1. change 'initial_balance' without using 'nonlocal', and
#    2. refer to anything (functions, values, etc) within the account with
#       just a string ('deposit', 'withdraw', 'balance').

def func_setup_account(initial_balance):
    def func_deposit(amount):
        dispatch['balance'] += amount
        return initial_balance
    def func_withdraw(amount):
        if amount > dispatch['balance']:
            return 'Insufficient funds'
        dispatch['balance'] -= amount
        return dispatch['balance']
    dispatch = {'deposit': func_deposit,
                'withdraw': func_withdraw,
                'balance': initial_balance}
    return dispatch

def func_deposit_to_account(account, amount):
    return account['deposit'](amount)
def func_withdraw_from_accoutn(account, amount):
    return account['withdraw'](amount)
def func_check_balance(account):
    return account['balance']

account1 = func_setup_account(20)
func_deposit_to_account(account1, 5)
func_withdraw_from_accoutn(account1, 17)
func_check_balance(account1)

# Propagating Constraints ----------------------------------------------------

# Below is an example of using everything above to make a calculator

from operator import add, sub, mul, truediv

def make_ternary_contraint(a, b, c, ab, ac, cb):
    ''' Constraint for ab(a,b)=c ; ac(a,c)=b ; cb(c,b)=a '''
    def new_value():
        av, bv, cv = [connector['has_val']() for connector in (a, b, c)]
        if av and bv:
            c['set_val'](constraint, ab(a['val'], b['val']))
        elif av and cv:
            b['set_val'](constraint, ac(a['val'], c['val']))
        elif bv and cv:
            a['set_val'](constraint, cb(c['val'], b['val']))
    def forget_value():
        for connector in (a, b, c):
            connector['forget'](constraint)
    constraint = {'new_val': new_value,
                  'forget': forget_value}
    for connector in (a, b, c):
        connector['connect'](constraint)
    return constraint

def adder(a, b, c):
    ''' The constraint that a + b = c '''
    return make_ternary_contraint(a, b, c, add, sub, sub)

def multiplier(a, b, c):
    ''' The constraint that a * b = c '''
    return make_ternary_contraint(a, b, c, mul, truediv, truediv)

def constant(connector, value):
    ''' The constraint that connector = value '''
    constraint = {}
    connector['set_val'](constraint, value)
    return constraint

def inform_all_except(source, message, constraints):
    ''' Inform all constraints of the message, except the source '''
    for c in constraints:
        if c != source:
            c[message]()

def connector(name = None):
    ''' A connector between constraints '''
    informant = None
    constraints = []
    def set_value(source, value):
        nonlocal informant
        val = connector['val']
        if val is None:
            informant, connector['val'] = source, value
            if name is not None:
                print(name, '=', value)
            inform_all_except(source, 'new_val', constraints)
        else:
            if val != value:
                print('Contradiction detected:', val, 'vs', value)
    def forget_value(source):
        nonlocal informant
        if informant == source:
            informant, connector['val'] = None, None
            if name is not None:
                print(name, 'is forgotten')
            inform_all_except(source, 'forget', constraints)
    connector = {'val': None,
                 'set_val': set_value,
                 'forget': forget_value,
                 'has_val': lambda: connector['val'] is not None,
                 'connect': lambda source: constraints.append(source)}
    return connector

def converter(c, f):
    ''' Connect c to f with constraints to convert from °C to °F '''
    u, v, w, x, y = [connector() for _ in range(5)]
    multiplier(c, w, u)
    multiplier(v, x, u)
    adder(v, y, f)
    constant(w, 9)
    constant(x, 5)
    constant(y, 32)

celcius = connector('Celcius')
fahrenheit = connector('Fahrenheit')

converter(celcius, fahrenheit)

celcius['set_val']('user', 25)
celcius['forget']('user')
fahrenheit['set_val']('user', 212)
fahrenheit['forget']('user')

#█████ 2.5 - Object Oriented Programming █████████████████████████████████████

# Classes --------------------------------------------------------------------

class Account:
    interest = .02
    def __init__(self, account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        else:
            self.balance -= amount
            return self.balance

acc1  = Account('Kirk')
acc2 = Account('Spock')
acc1 is acc2

acc1.holder
acc1.balance
acc1.balance = 200
acc1.deposit(100)
acc1.withdraw(250)

# getattr() & hasattr() can also access & check for class attributes
getattr(acc1, 'balance')
hasattr(acc1, 'deposit')

# The Class definition includes multi-argument functions
type(Account.deposit)
Account.deposit(acc1, 25)

# The functions are called 'methods' when they are bound to a self/instance
type(acc1.deposit)
acc1.deposit(25)

# Class attributes are assigned outside of __init__, and are accessible from
# all instances.
acc1.interest
acc2.interest
Account.interest = .04
acc1.interest
acc2.interest

# If a instace's attribute is assigned to something new, then that takes
# precidence over the class's attribute.
acc1.interest = .05
acc1.interest
acc2.interest
Account.interest = .1
acc1.interest
acc2.interest

# Class Inheritance ----------------------------------------------------------

# A class can re-use another class's attributes by putting the other class's
# name in parentheses after assignment.
class CheckingAccount(Account):
    '''Sets up an account that charges for withdraws.'''
    withdraw_charge = 1
    interest = .01
    def withdraw(self, amount):
        return Account.withdraw(self, amount + self.withdraw_charge)

acc3 = CheckingAccount('Sulu')
acc3.deposit(10)
acc3.withdraw(5)

# acc3 looks for withdraw in (1) it's instance, then (2) the CheckingAccount
# class, then (3) the Account class. It finds it in the CheckingAccount class,
# so 'withdraw()' takes $1.

# Class Multiple Inheritance -------------------------------------------------

# Multiple classes can be used for inheritance by assigning them in ().
# The ComboAccount class then looks in the CheckingAccount & SavingsAccount
# classes for functions before looking in the Account class.

class SavingsAccount(Account):
    deposit_charge = 2
    def deposit(self, amount):
        return Account.deposit(self, amount - self.deposit_charge)

class ComboAccount(CheckingAccount, SavingsAccount):
    '''An account that charges $2 for deposits and $1 for withdraws.'''
    pass

acc4 = ComboAccount('Uhura')
acc4.deposit(50)
acc4.withdraw(8)
acc4.deposit_charge
acc4.withdraw_charge

#█████ 2.7 - Object Abstraction ██████████████████████████████████████████████

# Special Methods ------------------------------------------------------------

# Some built in functions call methods on objects. Add these special methods
# to custom classes, so that they can be used by teh built-in functions.

from datetime import date
dat1 = date(2018, 11, 26)
str1 = 'Stringie'

str(dat1)
dat1.__str__()

repr(dat1)
dat1.__repr__()

len(str1)
str1.__len__()

str1[3]
str1.__getitem__(3)

# __call__() can allow a class to be used like a function.
class class_MakeAdder:
    def __init__(self, first_num):
        self.first_num = first_num
    def __call__(self, second_num):
        return self.first_num + second_num

func_add_5 = class_MakeAdder(5)
func_add_5(3)

