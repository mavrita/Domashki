oper = input().split()
result = 0
for i in oper:
    a = int(oper[0])
    b = int(oper[2])
    if oper[1] == '+':
        result = a + b
    elif oper[1] == '-':
        result = a - b
    elif oper[1] == '*':
        result = a * b
    elif oper[1] == '/':
        result = a / b
    else:
        result = 0
print(result)