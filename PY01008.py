def thuong(S):
    result = ""
    for i in range(len(S)):
        result += S[i].lower()  
    print(result)

def hoa(S):
    result = ""
    for i in range(len(S)):
        result += S[i].upper() 
    print(result)

S = input()  
cnt1 = cnt2 = 0


for i in range(len(S)):
    if S[i].isupper():
        cnt1 += 1 
    else:
        cnt2 += 1

if cnt1 > cnt2:
    hoa(S)
else:
    thuong(S)