#include <stdio.h>
int main(){
    int a = 4;
    printf("a is %d\n", a);
    first_function(a);
    return 0;
}

void first_function(int p){
    int b = 6;
    char *c = "Hello";
    printf("b is %d, c is %s, p is %d\n",b, c, p);
    second_function(b);
    return;
}

void second_function(int q){
    int d = 9;
    printf("d is %d, q is %d\n",d, q);
    return;
}
