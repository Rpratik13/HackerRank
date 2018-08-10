def lineUp(commands):
    count = 0;
    check = True;
    for i in range(len(commands)):
        if commands[i] == 'L' or commands[i] == 'R':
            check = not check;
        if check:
            count += 1;
    return count;


print(lineUp('A'))
