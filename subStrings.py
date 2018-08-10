def subStrings(string):
    ans = [];
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            ans.append(string[i:j]);
    return ans


inputString = input('Enter a String: ');
print('The sub-strings of {} are:'.format(inputString));

for subs in subStrings(inputString):
    print(subs);
