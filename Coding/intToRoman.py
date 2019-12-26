def intToRoman(num: int) -> str:
	roman = ['I', 'V', 'X', 'L', 'C', 'D', 'M', '', '']
	i = int()
	ans = str()
	while num:
		romanNum = {'0' : '',
					'1' : roman[i],
					'2' : roman[i] * 2,
					'3' : roman[i] * 3,
					'4' : roman[i] + roman[i + 1],
					'5' : roman[i + 1],
					'6' : roman[i + 1] + roman[i],
					'7' : roman[i + 1] + roman[i] * 2,
					'8' : roman[i + 1] + roman[i] * 3,
					'9' : roman[i] + roman[i + 2]}
		
		digit = num % 10
		ans = romanNum[str(digit)] + ans
		num //= 10
		i += 2
	return ans

num = int(input("Enter a number: "))
print(intToRoman(num))