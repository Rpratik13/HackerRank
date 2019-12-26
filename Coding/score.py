grade = [3.19, 3.36, 3.42, 3.85, 3.78, 3.5, 3.5, 3.5]
cred  = [20, 20, 18, 18, 18, 19, 18, 12]

sm = int()
sem = int(input('Enter semester: '))
for i in range(sem):
	sm += grade[i] * cred[i]

print(sm / sum(cred[:sem]))
