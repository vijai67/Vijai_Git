intt=int(input("Enter Any Number : "))

a=1
print(f'{intt}x{a}={intt*a}')
while a>0:
    a+=1
    print(f'{intt}x{a}={intt*a}')
    if a==10:
        break