#include <stdio.h>
#include <stdbool.h>
int main()
{
    int t = 0xaabbccdd;
    bool * p = (bool *)&t;
    printf("%x\n", *p);
    printf("%x\n", *(p+1));
    printf("%x\n", *(p+2));
    printf("%x\n", *(p+3));
}
