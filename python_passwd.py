import random
# l1 = [d+d for d in range(10)]
# # l2 = [sum (k+l) for k in range(0) & l in range(10)]
# print (l1)
# # print (l2)
# i = 0
# print(i+i in range(10))

A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a = "abcdefghijklmnopqrstuvwxyz"
N = "0123456789"
S = "*&%$#@![]|-_+"
all = A + a + N + S
leanght = 10
password = "".join sample(random.sample(all,leanght))
print ("Random Generated Password Is > ",password)