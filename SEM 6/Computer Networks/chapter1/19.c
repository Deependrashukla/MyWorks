//  Write a function reverse(s) that reverses the character string s. Use it to
//  write a program that reverses its input a line at a time.


#include <stdio.h>
#include <string.h>

#define MAX_LINE 1000  // Maximum line length

// Function to reverse a string in place
void reverse(char s[]) {
    int len = strlen(s);
    int i, j;
    char temp;
    
    for (i = 0, j = len - 1; i < j; i++, j--) {
        temp = s[i];
        s[i] = s[j];
        s[j] = temp;
    }
}

//  abcd --> dbca


// Function to read a line from input
int get_line(char s[], int limit) {
    int c, i;
    for (i = 0; i < limit - 1 && (c = getchar()) != EOF && c != '\n'; i++) {
        s[i] = c;
    }
    if (c == '\n') {
        s[i++] = c;  // Retain newline character
    }
    s[i] = '\0';
    return i;
}

// 1234567






int main() {
    char line[MAX_LINE];

    // printf("Enter text (Ctrl+D to stop on Linux/macOS, Ctrl+Z on Windows):\n");

    while (get_line(line, MAX_LINE) > 0) {
        reverse(line);
        printf("%s", line);  // Print reversed line
    }

    return 0;
}

