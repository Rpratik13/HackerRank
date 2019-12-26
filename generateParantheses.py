def generateParantheses(ans="", n):
	if (n == 0):
		return ans + ")"

	return generateParantheses(ans + "(", n - 1) + genere