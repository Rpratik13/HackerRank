def digitSum(num):
    ans = 0;
    while num != 0:
        ans += num % 10;
        num //= 10;
    return ans


def bestDivisor(num):
    sm = 0;
    ans = 0;
    for i in range(num):
        if (num % (i + 1)) == 0:
            digit_sm = digitSum(i + 1);
            if sm == digit_sm:
                if i < ans:
                    ans = i + 1;
            elif sm < digit_sm:
                ans = i + 1;
                sm = digit_sm;
    return ans


input_num = int(input());

result = bestDivisor(input_num);

print(result);
