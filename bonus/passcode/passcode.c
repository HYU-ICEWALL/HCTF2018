#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void init()
{
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
}

int main(void) {
	init();
	int option;
	char arr[33] = "";
	printf("get the passcode and break the door!\n\n");
	printf("----------Option----------\n");
	printf("1. cat ./passcode\n");
	printf("2. ./doorbreaker\n");
	printf("Input:\n");

	scanf("%d", &option);
	if (option == 1) {
		printf("cat: passcode: Permission denied\n");
		return 0;
	}

	else if (option == 2) {
		printf("door breaker executed!\n");
		printf("input the passcode!\n");
		printf("Input:\n");
		scanf("%5s", arr);
		if( !strncmp(arr, "cat:", strlen("cat:")) ) {
			scanf("%10s", arr);
			if( !strncmp(arr, "passcode:", strlen("passcode:")) ) {
				scanf("%11s", arr);
				if( !strncmp(arr, "Permission", strlen("Permission")) ) {
					scanf("%7s", arr);
					if( !strncmp(arr, "denied", strlen("denied")) ) {
						system("cat /home/passcode/flag");
						return 0;
					}
				}
			}
		}

		printf("door not broken!\n");
	}

	return 0;
}
