import math

def is_prime(a):
    if a <= 1:
        return False
    if a == 2:
        return True  # 2 là số nguyên tố
    if a % 2 == 0:
        return False
    for x in range(3, int(math.sqrt(a)) + 1, 2):
        if a % x == 0:
            return False
    return True

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def count_coprimes(N):
    count = 0
    for i in range(1, N):
        if gcd(i, N) == 1:
            count += 1
    return count

test = int(input())

while test > 0:
    N = int(input())
    K = count_coprimes(N)
    
    if is_prime(K):
        print("YES")
    else:
        print("NO")
    
    test -= 1
