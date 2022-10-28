import pandas
list1 = [1,2,3,4,5]
data1 = pandas.DataFrame(list1)
print ("DataFrame List Example\n",data1)


dict1 = {'names':['bhuvan','mallesh','chetan','praveen','akshay'],'Roll Number':[21,52,78,9,10],'age':[24,21,23,24.5,28]}
data2 = pandas.DataFrame(dict1)
print ("DataFrame Dictionary Example\n",data2)