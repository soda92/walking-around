#define uint unsigned int
#include <stdio.h>
int main()
{
    long t = 0x10;
    uint *pr = (uint *)&t;
    pr[0] = 1;
    pr[1] = 0;
    pr[2] = 1;
    pr[3] = 0;
    printf("%ld\n", t);
}
