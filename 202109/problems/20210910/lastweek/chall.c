#include <stdio.h>
#include <string.h>

//char *flag = "mctf{Did_you_watch_rev_with_ghidra_video?}";
char check[42] = "\x44\x52\x4d\x5f\x51\x7d\x58\x5d\x75\x48\x46\x4c\x75\x4e\x50\x4d\x52\x59\x75\x43\x5c\x4f\x75\x4e\x58\x4d\x59\x75\x5e\x59\x58\x5d\x43\x50\x75\x4f\x58\x5d\x5c\x46\x15\x57";

int repos(int pos){
    return 0x19 - pos;
}

char reverse(char arg){
    int pos;
    if (0x41 <= (int)arg && (int)arg <= 0x5a){
        pos = (int)arg - 0x41;
        return (char)(repos(pos) + 0x41);
    } else {
        if (0x61 <= (int)arg && (int)arg <= 0x7a){
            pos = (int)arg - 0x61;
        return (char)(repos(pos) + 0x61);
        } else {
            return arg;
        }
    }
}

int main(void){
    char reversed[64];
    char in[64];
    int len;
    printf("I am a Funny King!\n");
    printf("give me a sweet candy!\n");
    fgets(in, 0x40, stdin);
    len = strlen(in);
    in[len-1]='\0';
    for (int i=0;i<len;i++){
        reversed[i] = reverse(in[i]);
    }
    memfrob(check, 42);
    //printf("%s %d\n",check, strlen(check));
    //printf("%s %d\n",reversed, strlen(reversed));
    int res = strcmp(check,reversed);
    if (res == 0) {
        printf("Thank you for giving me a nice candy!!");
    } else {
        printf("No. This is not sweet...");
    }
}