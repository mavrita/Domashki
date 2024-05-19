slovo = input()
alpha = set('abcdefghijklmnopqrstuvwxyz')
numbers = set('1234567890')
a = set()
n = set()
other = set()
for i in slovo:
    if i in alpha:
        a.add(i)
    elif i in numbers:
        n.add(i)
    else:
        other.add(i)
print(a)
print(n)
print(other)