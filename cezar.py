def code(string, n):
    res = []
    for i in string:
        res += chr(ord(i) + n)
    return res
string = input()
n = int(input())
print(code(string, n))