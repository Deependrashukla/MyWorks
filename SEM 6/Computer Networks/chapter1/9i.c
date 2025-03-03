// Write a program to copy its input to its output, replacing each string of one or
//  more blanks by a single blank. 



// #include <stdio.h>
// #include <stdbool.h>


int main(){
    bool isblank = true;
    int c;
    while((c = getchar()) != EOF){
        if (c == ' '){
            if (isblank){
                putchar(c);
                isblank = false;
            }
            
        }else{
            putchar(c);
            isblank = true;
        }
        
    }
    return 0;
}
























// #include <stdio.h>
// #include <stdbool.h>

// int main() {
//     int c;
//     bool isblank = true;

//     while ((c = getchar()) != EOF) {
//         if (c == ' ') {
//             if (isblank) {
//                 putchar(c);
//                 isblank = false;
//             }
//         } else {
//             putchar(c);
//             isblank = true;
//         }
//     }

//     return 0;
// }
