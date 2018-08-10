def zFunction(s):
    res = [];
    for i in range(len(s)):
        count = 0;
        for a, b in zip(s[i:], s):
            if a != b:
                break
            count += 1
        res.append(count);
    return res


s = 'ababac';
result = zFunction(s);
print(result);
