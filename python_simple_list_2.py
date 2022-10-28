S1 = int(input("Enter The Marks 1 : "))
S2 = int(input("Enter The Marks 2 : "))
S3 = int(input("Enter The Marks 3 : "))
S4 = int(input("Enter The Marks 4 : "))
S5 = int(input("Enter The Marks 5 : "))
S6 = int(input("Enter The Marks 6 : "))

StudList = [S1,S2,S3,S4,S5,S6]
print(StudList)

StudList.sort()
print(StudList,'\n')

Avarage = sum(StudList)/len(StudList)
print('The Avarage Marks Of All The Subs',Avarage)