def hourInWords(n):
	if (n>12):
		n = n % 12;

	if(n==1):
		return "one";
	elif(n==2):
		return "two";
	elif(n==3):
		return "three";
	elif(n==4):
		return "four";
	elif(n==5):
		return "five";
	elif(n==6):
		return "six";
	elif(n==7):
		return "seven";
	elif(n==8):
		return "eight";
	elif(n==9):
		return "nine";
	elif(n==10):
		return "ten";
	elif(n==11):
		return "eleven";
	elif(n==12):
		return "twelve";
def minuteInWords(n):
	if(n==1):
		return "one";
	elif(n==2):
		return "two";
	elif(n==3):
		return "three";
	elif(n==4):
		return "four";
	elif(n==5):
		return "five";
	elif(n==6):
		return "six";
	elif(n==7):
		return "seven";
	elif(n==8):
		return "eight";
	elif(n==9):
		return "nine";
	elif(n==10):
		return "ten";
	elif(n==11):
		return "eleven";
	elif(n==12):
		return "twelve";
	elif(n==13):
		return "thirteen";
	elif(n==14):
		return "fourteen";
	elif(n==15):
		return "fifteen";
	elif(n==16):
		return "sixteen";
	elif(n==17):
		return "seventeen";
	elif(n==18):
		return "eighteen";
	elif(n==19):
		return "nineteen";
	elif(n==20):
		return "twenty";
	elif(n==21):
		return "twenty one";
	elif(n==22):
		return "twenty two";
	elif(n==23):
		return "twenty three";
	elif(n==24):
		return "twenty four";
	elif(n==25):
		return "twenty five";
	elif(n==26):
		return "twenty six";
	elif(n==27):
		return "twenty seven";
	elif(n==28):
		return "twenty eight";
	elif(n==29):
		return "twenty nine";
	elif(n==30):
		return "thirty";




def timeInWords(h,m):
	if (m==0):
		return minuteInWords(h) + " o' clock";
	elif(m==15):
		return "quarter past " + hourInWords(h);
	elif(m==30):
		return "half past " + hourInWords(h);
	elif(m==45):
		return "quarter to " + hourInWords(h+1);
	elif(m==1):
		return minuteInWords(m) + " minute past " + hourInWords(h);
	elif(m>1 and m<15) or (m>15 and m<30):
		return minuteInWords(m) + " minutes past " + hourInWords(h);
	elif(m>30 and m<45) or (m>45 and m<=59):
		return minuteInWords(60-m) + " minutes to "+ hourInWords(h+1);


h = int(input());
m = int(input());

result = timeInWords(h,m);

print(result);