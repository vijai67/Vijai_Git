num = int(input("Enter A Number : "))
prime=True
for i in range(2,num):
    if (num%i==0 and num!=2):
        prime=False

if prime:
    print(num,"Is A Prime Number")
else:
    print(num,"Not A Prime Numner")