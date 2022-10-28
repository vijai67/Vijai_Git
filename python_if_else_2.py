M1 = int(input("Enter The Marks Sub1 : "))
# M2 = int(input("Enter The Marks Sub2 : "))
# M3 = int(input("Enter The Marks Sub3 : "))
# M = M1+M2+M3+M4
# if (((M1/100)*100)>=33) or (((M1/100)*100)==40):
if (M1 >= 33 and M1 <= 40) or (M1 > 40):
    print("M1 Pass")
# elif (((M1/100)*100)<33):
elif (M1<33):
    print("M1 Fail")