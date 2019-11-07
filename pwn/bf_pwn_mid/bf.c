#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<string.h>


static char origin[0x20] = ""; // Welcome to HCTF! you should find this origin flag!


void init()
{
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
}

int compare(char *pwd)
{
	for(int i = 0; strlen(origin); i ++)
	{
		sleep(1);
		if(pwd[i] == origin[i])
		{
			continue;
		}
		else
		{
			printf("Wrong Password!\n");
			return 0;
		}
	}
	printf("Correct Password!\n");
}


int main()
{
	char password[0x20];
	init();
	printf("Input Password [A-Z0-9_{}]\n");

	read(0, password, sizeof(password));

	compare(password);
}
