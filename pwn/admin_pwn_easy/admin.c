#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

char id[50];
char password[50];

int login_chk;
int (*fptr[5])();


int login() {

	if(login_chk == 1) {
		printf("[-] Login already \n");
		return 0;
	}
	
	printf("ID: ");
	read(0, id, sizeof(id)-1);

	printf("Password: ");
	read(0, password, sizeof(password)-1 );

	if( !strncmp(id, "admin",strlen("admin")) && !strncmp(password, "admin!",strlen("admin!")) ) {
		printf("[+] Access\n");
		login_chk = 1;
	}
	else {
		printf("[-] Access Denied\n");
	}
	login_chk = 0;
}

int logout() {
	if( !login_chk ) {
		printf("[-] Login First\n");
		return 0;
	}

	memset(id, 0, sizeof(id));
	memset(password, 0, sizeof(password));

	login_chk = 0;

	printf("[+] Logout\n");
}

int exit_func() {
	printf("Bye Bye~\n");
	exit(0);
}

int init() {
	fptr[1] = login;
	fptr[2] = logout;
	fptr[3] = exit_func;
}

void menu()
{
	puts("");
	printf("1. Login\n");
	printf("2. Logout\n");
	printf("3. Exit\n");
}

int main()
{
	int sel;
	init();
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);


	while(1) {
		menu();

		printf(">");
		scanf("%d",&sel);

		if( sel > 3 ) {
			return 0;
		}

		fptr[sel]();
	}
}