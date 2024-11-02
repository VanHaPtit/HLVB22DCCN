def tinh(s):
    a = int(s[0]) * 10 + int(s[1])
    b = int(s[-2]) * 10 + int(s[-1])
    if a == b:
        print("YES")
    else:
        print("NO")

test = int(input())
for _ in range(test):
    s = input() 
    tinh(s)

