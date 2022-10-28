# keep all the keys lower case cause to write them easily
a = 125846
d1 = {"vijai":"vedha",
'ghar':'bar',
"kuch":'mat puch',
"namber":524,
'list':[1,],
"tupl":(1,),
"extra":a,
"vsl":{'a':a,"fruit":"jar",
1:700},
1:700
}

# print(d1['vijai'])
# print(d1['extra'])
# print(d1['tupl'])
# print(d1['namber'])
# print(d1['list'])
# print(d1['list'][0])
# print(d1['vsl']['a'])
# print(d1['vsl']['fruit'])

# d1["extra"]=[21,52]
# print(d1["extra"])


# # methods of dictionary
# print(d1.keys())
# print(type(d1.keys()))
# print(list(d1.keys()))
# print(type(list(d1.keys())))

# print(d1.values())
# print(list(d1.values()))
# print(type(d1.values()))

# print(list(d1.items()))
# print(d1.items())

updated_dict={
"love":"hate",
'list':[1,2,3,4,] #this line will update the older values for 'list' in d1
}

d1.update(updated_dict)
print(list(d1.items()))

print(d1['vijai']) # this will same as get but if "key" is not present in the dict this will gives "error"
print(d1.get("vijai")) #this will gives "none" if the value is not present in the dict
print(d1.get("vedha"))