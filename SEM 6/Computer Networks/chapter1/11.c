#include <stdio.h>
#include <string.h>

#define IN   1  /* Inside a word */
#define OUT  0  /* Outside a word */

/* Function to count lines, words, and characters in input */
// void count_words(const char *input, int *nl, int *nw, int *nc) {
//     int c, state;
//     state = OUT;
//     *nl = *nw = *nc = 0;

//     for (int i = 0; input[i] != '\0'; ++i) {
//         c = input[i];
//         ++(*nc);
//         if (c == '\n')
//             ++(*nl);
//         if (c == ' ' || c == '\n' || c == '\t')
//             state = OUT;
//         else if (state == OUT) {
//             state = IN;
//             ++(*nw);
//         }
//     }
// }




/* Function to count lines, words, and characters in input */

#include <stdbool.h>
int main(){
    char input[100];
    int c;
    int line, word, letter;
    bool in = true;
    scanf("%c send input", &input);
    for(int i = 0; input[i] != '\0'; ++i ){
        c = input[i];
        ++ letter;
        if (c == '\n'){
            ++line;
        }else if(c == ' ' || c == '\n' || c == '\t'){
            if (in){
                ++word;
            }
            in = false;
        }else{
            in = true;
        }
    }
    return 0;
}

