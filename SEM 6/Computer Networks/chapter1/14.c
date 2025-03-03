//  Write a program to print a histogram of the frequencies of different characters
//  in its input.

#include <stdio.h>

#define MAX_CHAR 256  // Maximum number of different characters

int main() {
    int c, i, j;
    int char_freq[MAX_CHAR] = {0};

    // Read input and count character frequencies
    while ((c = getchar()) != EOF) {
        if (c >= 0 && c < MAX_CHAR) {
            char_freq[c]++;
        }
    }

    // Print the histogram
    printf("Histogram of Character Frequencies:\n");
    for (i = 0; i < MAX_CHAR; i++) {
        if (char_freq[i] > 0) {
            printf("%c: ", i);
            for (j = 0; j < char_freq[i]; j++) {
                putchar('*');
            }
            putchar('\n');
        }
    }

    return 0;
}
