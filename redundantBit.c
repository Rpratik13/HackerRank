#include <stdio.h>

int main(){
	char inp[101] = {};
	int c_one=0,length=0;
	int i;
	printf("Enter a message in binary(max length = 100): ");
	scanf("%s",inp);
	for(i=0;inp[i]!='\0';i++){
		if (inp[i]=='1'){
			c_one++;

		}
		length++;
	}

	if (c_one%2==0){
		inp[length]='1';
	}
	else{
		inp[length]='0';
	}

	printf("The sent message is %s. \n",inp);
}
