a = "Hello Buddy"
print(a[0:-1]) #if you don't know the lenght of the string (note: add one space before ending ' " ')
# print(a[0:12:6]) # this is to print gapped letters 

b = "H     A     P     P     Y "
print(b[0:-1:6])
print(a[0::2])
print(b[0:])

# String Functions (len(<variable name>)) | (<variable name>.endswith('any charecter or word')) |  
print(len(a))
print(len(b))

print(b.endswith(' '))
print(a.endswith(' '))

print(a.count('Hello'))
print(b.count('H'))

print(a.capitalize())
print(b.capitalize())

print(a.find('Buddy'))
print(b.find('y'))

print(a.replace('Hello', 'Vijai'))
# c = a.replace('Harry', 'Vedha')
print(a)