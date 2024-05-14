lst = [27, 86, 1, 39548, -28, 450, 0, -28, 783]
min = lst[0]
for i in range(len(lst)):
    if min > lst[i]:
       min = lst[i]
print(min)