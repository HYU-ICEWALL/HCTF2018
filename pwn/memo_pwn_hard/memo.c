#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<string.h>


typedef struct memo{
	char *ptr;
	void (*func)();
}MEMO;

int memo_count = 0;
MEMO *MEMOS[8];

void delete()
{	
	int num;
	if(memo_count == 0)
	{
		printf("Add memo first!\n");
		return;
	}

	printf("Select number 0-%d", memo_count-1);
	scanf("%d", &num);
	
	if(num > memo_count-1)
	{
		printf("nope\n");
		return;
	}
	
	free(MEMOS[num]->ptr);
	free(MEMOS[num]);
}

void show()
{
	int num;
	if(memo_count == 0)
	{
		printf("Add memo first!\n");
		return;
	}

	printf("Select number 0-%d", memo_count-1);
	scanf("%d", &num);

	if(num > memo_count-1)
	{
		printf("nope\n");
		return;
	}

	MEMOS[num]->func(MEMOS[num]->ptr);
}

void print(char *ptr)
{
	printf("%s\n", ptr);
}


void add()
{
	unsigned int size;
	if(memo_count > 5)
	{
		printf("Too many memos");
		return;
	}

	MEMOS[memo_count] = (MEMO *)malloc(sizeof(MEMO));
	printf("Memo Size : \n");
	scanf("%d", &size);
	if(size > 0x50)
	{
		printf("Size is too large < 0x100\n");
		return;
	}

	MEMOS[memo_count]->ptr = (char *)malloc(size+1);
	MEMOS[memo_count]->func = print;
	
	printf("Input memo\n");
	read(0, MEMOS[memo_count]->ptr, size);

	memo_count++;
}

void init()
{
	setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
}

int print_menu()
{
	printf("1. Add\n");
	printf("2. Show\n");
	printf("3. Delete\n");
	printf("4. Exit\n");

	return 0;
}

int main()
{
	char buf[32];
	int num;

	init();

	while(!print_menu())
	{
		read(0, buf, 32);
		num = atoi(buf);
		switch(num)
		{
			case 1:
				add();
				break;
			case 2:
				show();
				break;
			case 3:
				delete();
				break;
			case 4:
				exit(1);
				break;
		}
		
	}


}
