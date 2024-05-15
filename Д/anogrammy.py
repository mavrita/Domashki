w1 = input()
w2 = input()
n1 = [s for s in w1 if s != " "]
n2 = [s for s in w2 if s != " "]
l1 = list(n1)
l2 = list(n2)
d1 = {}
d2 = {}
for i in l1:
    if i not in d1:
        d1[i] = 1
    else:
        d1[i] += 1
for i in l2 :
    if i not in d2:
        d2[i] = 1
    else:
        d2[i] += 1
print(d1, d2)
print(d1 == d2)