def reverseParentheses(s):
    brac = [];
    for i in range(len(s)):
        if s[i] == '(':
            brac.append(i);
        if s[i] == ')':
            pos = brac.pop();
            if (pos == 0):
                s = s.replace(s[pos:i + 1], s[i::-1]);
            else:
                s = s.replace(s[pos:i + 1], s[i:pos - 1:-1]);

    s = s.replace('(', '');
    s = s.replace(')', '');
    return s;


st = input();
print(reverseParentheses(st));
