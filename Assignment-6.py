# Exercise1

a = 2
b = 3

print(a+b)


# Exercise2

str2 = "nFactorial"
rev = str2[::-1]
print(rev)


# Exercise3

str3 = "Python"
print(len(str3))


# Exercise4

string1 = "Hello"
string2 = " World"

print(string1 + string2)


# Exercise5

char = input()
def find_vowel(a):
    if a == "a" or a == "e" or a == "i" or a == "o" or a == "u":
        print("vowel")
    else: print("not vowel")

find_vowel(char)


# Exercise 6

str6 = input()
def swap(st):
    new_st = f'{str6[-1]}{str6[1:-1]}{str6[0]}'
    print(new_st)

swap(str6)


# Exercise 7

str7 = input()

def to_upper(st):
    new_st = st.upper()
    print(new_st)

to_upper(str7)


# Exercise 8

rec_length = int(input())
rec_width = int(input())

def rec_area(a, b):
    area = a * b;
    print(area)

rec_area(rec_length, rec_width)


# Exercise 9

num9 = int(input())

def even(a):
    if a % 2 == 0:
        print("even")
    else: print("odd")

even(num9)


# Exercise 10

str10 = input()

def extract(st):
    print(st[0:3])

extract(str10)

# Exercise 11

name = input()
age = int(input())

print(f'My name is {name} and I am {age}.')


# Exercise 12

