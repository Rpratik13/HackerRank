'''
a b c                    digit carry
0 0 0 a == b and a == c   a    a
1 1 1 a == b and a == c

0 0 1 a == b and a != c   c    a
1 1 0 a == b and a != c

0 1 0 a != b and a == c   b    a
1 0 1 a != b and a == c

0 1 1 a != b and b == c   a    b
1 0 0 a != b and b == c
'''

def addBinary(a: str, b: str) -> str:
    a = '0' * (len(b) - len(a)) + a
    b = '0' * (len(a) - len(b)) + b
    carry = '0'
    ans = str()
    
    for i in range(len(a) - 1, -1, -1):
        if a[i] == b[i] and a[i] == carry:
            ans = a[i] + ans
            carry = a[i]
        elif a[i] == b[i] and a[i] != carry:
            ans = carry + ans
            carry = a[i]
        elif a[i] != b[i] and a[i] == carry:
            ans = b[i] + ans
            carry = a[i]
        else:
            ans = a[i] + ans
            carry = b[i]
    
    if carry == '1':
        return carry + ans
    return ans