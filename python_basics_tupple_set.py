l = (1,3,4) #tuple
m = 1,2,3 #tuple

a = {} #dict
b = {1,2,3,3,} #set
c = set() #empty set
d = set(l) #set with inserting or adding 'l' values i.e tuple
e = set(m) #set with inserting or adding 'm' values i.e tuple

t = "hi",

print(a,b,c,d,e,l,m,t)
print(type(a),a,'a')
print(type(b),b,'b')
print(type(c),c,'c')
print(type(d),d,'d')
print(type(e),e,'e')
print(type(l),l,'l')
print(type(m),m,'m')
print(type(t),t,'t')

e.add(l) #add function to add a single value to set at a time
print(e)
e.add('hi')
print(e)

print(len(e))

e.remove('hi')
print(e)

e.pop()
print(e)

o = e.union((25,'lol',11,15,2,10,'hi')) # it will added to e set and print will print the values in accending order
q = e.union({'ka',85,5,64,25,852,10,'hi'}) # these numbers are added to e and print will give without arrenging the integer values
print(o)
print(q)

# e.clear()
# print(e)

g = e.intersection(l) # this will give the intersection values from both the sets "returns COMMON VALUES FROM BOTH THE SETS"
print(g)