#include<stdio.h>
#include<string.h>

// shellcode bytes to test
unsigned char code[] = "";

int main()
{
    printf("Shellcode Length:  %d\n", strlen(code));
	int (*ret)() = (int(*)())code;
	ret();
}
