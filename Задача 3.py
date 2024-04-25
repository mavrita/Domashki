n = int(input())
f = 0
s = []
for i in range(1, n+1):
    f = + i
    s.append(f)
factorial = s[0]
for i in s:
    factorial = factorial * i
print(factorial)
