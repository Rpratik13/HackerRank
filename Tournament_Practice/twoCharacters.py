import os


def twoCharacters(s):
    alpha = list(set([i for i in s]))
    ans = 0
    for i in range(len(alpha)):
        for j in range(len(alpha)):
            if alpha[i] == alpha[j]:
                continue
            count = 0
            string = ''
            check = True
            for k in s:
                if k == alpha[i]:
                    if check:
                        count += 1
                        check = False
                        string += k
                    else:
                        break
                elif k == alpha[j]:
                    if check:
                        break
                    else:
                        count += 1
                        string += k
                        check = True
            else:
                ans_string = string
                ans = max(ans, count)
    # print(ans_string)
    return ans


if __name__ == '__main__':
   
    l = int(input().strip())

    s = input()

    result = twoCharacters(s)

    print(result)
