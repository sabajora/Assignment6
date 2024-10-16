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

char = "b"
def find_vowel(a):
    if a == "a" or a == "e" or a == "i" or a == "o" or a == "u":
        print("vowel")
    else: print("not vowel")

find_vowel(char)


# Exercise 6

str6 = "hello"
def swap(st):
    temp_char = st[0]
    st[0] = st[-1]
    st[-1] = temp_char
    print(st)

swap(str6)