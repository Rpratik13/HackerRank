def isCryptSolution(crypt, solution):
    sm = 0;
    sm_3 = 0;
    for i in range(2):
        word = '';
        for j in range(len(crypt[i])):
            x = 0;
            while (solution[x][0] != crypt[i][j]):
                x += 1;
            word += solution[x][1];
        sm += int(word);

    word = '';
    for j in range(len(crypt[2])):
        x = 0;
        while (solution[x][0] != crypt[2][j]):
            x += 1;
        word += solution[x][1];
    sm_3 += int(word);

    print(sm);
    print(sm_3);

    return sm == sm_3


print(isCryptSolution(["TEN", "TWO", "ONE"], [['O', '1'],
                                              ['T', '0'],
                                              ['W', '9'],
                                              ['E', '5'],
                                              ['N', '4']]))
