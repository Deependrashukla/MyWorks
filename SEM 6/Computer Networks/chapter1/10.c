//  Write a program to copy its input to its output, replacing each tab by \t, each
//  backspace by \b, and each backslash by \\. This makes tabs and backspaces visible in an
//  unambiguous way. 


#include <stdio.h>
// ? Random output is printed by this.
// int main(){
//     int c;
//     while((c = getchar()) != EOF){
//         printf("%d hell", c);
//     }
//     return 0;
// }


// int main(){
//     int c;
//     while((c = getchar()) != EOF){
//         if (c == '\t'){
//             printf("\\t");
//         } else if (c == '\b'){
//             printf("\\b");
//         } else if (c == '\\'){
//             printf("\\\\");
//         } else{
//             putchar(c);
//         }
//     }
//     return 0;
// }

// #include <stdio.h>

// ? i did not get \b.
// int main() {
//     int c;
//     while ((c = getchar()) != EOF) {
//         if (c == '\t') {
//             printf("\\t\n");
//         } else if (c == '\b') {
//             printf("\\b\n");
//         } else if (c == '\\') {
//             printf("\\\\\n");
//         } else {
//             putchar(c);
//         }
//     }

//     return 0;
// }







#include <stdio.h>

int main(){
    int c;
    while ((c = getchar()) != EOF){
        if (c == '\b'){
            printf("\b");
        }else if  (c == '\t'){
            printf("\\t");
        }else if(c == '\\'){
            printf("\\");
        }else{
            putchar(c);
        }
    }
    return 0;
}
