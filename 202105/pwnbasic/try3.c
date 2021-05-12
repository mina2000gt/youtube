#include <stdio.h>
void vul();
void secret();
int main(){
	vul();
	return 0;
}
void vul(){
	char c[8];
	printf("What's your name?\n");
	gets(c);
	printf("Welcome, %s\n", c);
	return;
}
void secret(){
	execve("/bin/sh",0,0);
	return;
}
