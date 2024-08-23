#include <stdio.h>
int main()
{
    int *ptr, q;
    q = 50;
    ptr = &q; /* address of q is assigned to ptr */
    printf("%d", *ptr); /* display q's value using ptr variable */
    return 0;
}
