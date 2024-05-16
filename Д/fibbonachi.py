n = int(input())
lst = [i for i in range (1, n+1)]
print(lst)
print('---------')
f1 = 1
f2 = 1
fib = [f1,f2]
sum = 0
while len(fib) <= n:
    sum = f1 + f2
    fib.append(sum)
    f1 = f2
    f2 = sum
print(fib)