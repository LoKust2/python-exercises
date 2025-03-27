# Write programs that read a line of input as a string and print:

string = input("Enter a line: ")
characters = list(string)
upper = list()
vowels = list()

# a) Only the uppercase letters in the string.

for c in characters:
    if c.isupper():
        upper.append(c)

print("\na) Every uppercase letter: ", end='')
for c in upper:
    print(c, end = ' ')

# b) Every second letter of the string.

i = 1
print("\nb) Every second letter: ", end='')
for c in characters:
    if i%2 == 0:
        if c == ' ':
            continue
        elif str.isdigit(c):
            continue
        else:
            print(c, end = ' ')
    i += 1

# c) The string, with all vowels replaced by an underscore.
for c in range(len(characters)):
    if characters[c] in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        vowels.append(c)
        characters[c] = '_'

print("\nc) The string, with all vowels replaced by an underscore: ")
print(''.join(characters))
    
# d) The number of digits in the string.
k = 0
for c in characters:
    if str.isdigit(c):
        k += 1

print(f"d) The number of digits in the string: {k}")

# e) The positions of all vowels in the string.

print("e) The positions of all vowels in the string: ")
for c in vowels:
    print(c, end = ' ')
