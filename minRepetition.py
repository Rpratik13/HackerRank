def isSubstring(string1, string2):
    for i in range(len(string2) - len(string1) + 1):
        if string1 == string2[i:i + len(string1)]:
            return True
    return False


def minRepetition(string1, string2):
    stringx = string1
    ans = 1

    while len(stringx) < len(string2):
        stringx += string1
        ans += 1

    if isSubstring(string2, stringx):
        return ans

    if isSubstring(string2, stringx + string1):
        return ans + 1

    return -1


if __name__ == '__main__':
    print(minRepetition("abcd", "cdabcdab"))
