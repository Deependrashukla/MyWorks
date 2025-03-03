// #include <stdio.h>
// int main(){
//     int c = getchar();
//     while (c != EOF){
//         printf("%c",c);
//         // putchar(c);
//         c = getchar();
//     };
//     return 0;
// }

// """ Verify that the expression getchar() != EOF is 0 or 1."""


#include <stdio.h>
int main(){
    int c;
    while ((c = getchar()) != EOF){
        // putchar(c);
        printf("%d", c != EOF );

    }
    return 0;
}