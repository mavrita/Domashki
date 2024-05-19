s1 = input().split(',')
s2 = input().split(',')
t1 = set(s1)
t2 = set(s2)
b = list()
if t1.intersection(t2):
    b.append(t1.intersection(t2))
print(len(b)+1)