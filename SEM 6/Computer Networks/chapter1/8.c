//  Write a program to count blanks, alphabets, tabs, and newlines. 


#include <stdio.h>

int main(){
    int c;
    int blanks = 0, tabs = 0, newline = 0, letter = 0;
    while ((c = getchar()) != EOF){
        if (c == ' '){
            blanks ++ ;
        }else if (c == '\t'){
            tabs ++;
        }else if (c == '\n'){
            newline ++;
        }else {
            letter ++;
        }
    }
    printf("count of blanks %d\n", blanks);
    printf("count of tabs %d\n", tabs);
    printf("count of newline %d\n", newline);
    printf("count of char %d\n", letter);
    return 0;
}
