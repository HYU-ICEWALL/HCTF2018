#include <stdio.h>

void init()
{
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
}

int main(void) {
	init();
	printf("HCTF{N0W_Y0U_KN0W_H0W_T0_NC?HEHE}\n");
	return 0;
}