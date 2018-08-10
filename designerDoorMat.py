inp = [int(x) for x in input().split()];
n = inp[0];
m = inp[1];

for i in range(1, n + 1):
    if i < (n + 1) // 2:
        print('-' * ((m - (3 * (2 * i - 1))) // 2), end="")
        print('.|.' * (2 * i - 1), end="")
        print('-' * ((m - (3 * (2 * i - 1))) // 2))
    elif i == (n + 1) // 2:
        print('-' * ((m - 7) // 2), end="");
        print('WELCOME', end='');
        print('-' * ((m - 7) // 2));
    else:
        print('-' * ((m - (3 * (2 * (((n + 1) // 2) - (i % ((n + 1) // 2))) - 1))) // 2), end="")
        print('.|.' * (2 * (((n + 1) // 2) - (i % ((n + 1) // 2))) - 1), end="")
        print('-' * ((m - (3 * (2 * (((n + 1) // 2) - (i % ((n + 1) // 2))) - 1))) // 2))
