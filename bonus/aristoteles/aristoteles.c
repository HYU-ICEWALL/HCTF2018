#include <stdio.h>
#include <unistd.h>

void init()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

int main() {
    init();
    printf("아리스토텔레스도 깜짝 놀라는 삼단 논법\n");
    printf("Ubuntu 16.04\n");

    int A;
    float B;
    int C;

    while (1) {
        printf("A is int type, B is float type, C is int type\n");
        printf("\nA == B && B == C && C != A\n를 만족하는 A, B, C를 입력하라!\n");
        scanf("%d %f %d", &A, &B, &C);
        printf("Checking\n");
        sleep(3);
        if (A == B && B == C && C != A) {
            printf("삼단논법을 간파!\n\n");
            system("cat /home/aristoteles/flag");
            return 0;
        }
        else {
            printf("No...\n");
            if (A != B) printf("A != B\n");
            if (B != C) printf("B != C\n");
            if (C == A) printf("C == A\n");
        }
    }

    return 0;
}

