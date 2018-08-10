def isIPv4Address(inputString):
    val = '';
    count_dot = 0;
    for i in range(len(inputString)):
        if inputString[i] == '.':
            count_dot += 1;
            if val == '':
                return False;
            elif not (0 <= int(val) < 256):
                return False;
            val = '';
        else:
            if not (47 < ord(inputString[i]) < 58):
                return False
            val += inputString[i];

        if i == len(inputString) - 1:
            if val == '':
                return False;
            elif not (0 <= int(val) < 256):
                return False;

    if count_dot != 3:
        return False
    return True


print(isIPv4Address('0.1.1.25'))
