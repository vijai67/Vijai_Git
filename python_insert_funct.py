# Create a List & Change the 0th Index Value
List1 = [5,22.2,"Vedha",True,False]
print(List1,'\n')

# Print The Index Value
print(List1[1],'\n')

# Change The Value Of The Given List
List1[0] = 100
print(List1)

# Append Values To The List
List2 = []
List2.append(25)
print(List2)

# Append Insert Sort & Reverse Of List
l1 = [1,8,5,3,4,2,789,56,657,5,521,45,120,2.2,False,True,]
print('The List Displayed : ',l1,'\n')
l1.sort()
print('The List Is Sorted : ',l1,'\n')
l1.reverse()
print('The List Is Reverse Sorted : ',l1)
l1.insert(4,'HEllo ViJAi VEdHA')
print('The String Is Inserted In The 4th Index Of List : ',l1)
l1.append(8000000000000000)
print('The List Is Appended With The Given Value : ',l1)

# List Fuctions Pop & Remove 
l1.pop()
print('The List Is Poped By Last Element : ',l1)
l1.remove(True)
print('The List Is Removed Given Value From The List : ',l1)