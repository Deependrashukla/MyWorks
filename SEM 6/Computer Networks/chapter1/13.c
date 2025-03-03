//  Write a program to print a histogram of the lengths of words in its input. It is
//  easy to draw the histogram with the bars horizontal; a vertical orientation is more challenging. 

#include <stdio.h>

#define MAX_WORD_LENGTH 20

int main() {
    int c, i, j, word_length;
    int word_lengths[MAX_WORD_LENGTH + 1] = {0};

    word_length = 0;
    while ((c = getchar()) != EOF) {
        if (c == ' ' || c == '\n' || c == '\t') {
            if (word_length > 0) {
                if (word_length <= MAX_WORD_LENGTH) {
                    word_lengths[word_length]++;
                } else {
                    word_lengths[MAX_WORD_LENGTH]++;
                }
                word_length = 0;
            }
        } else {
            word_length++;
        }
    }

    printf("Horizontal Histogram of Word Lengths:\n");
    for (i = 1; i <= MAX_WORD_LENGTH; i++) {
        printf("%2d: ", i);
        for (j = 0; j < word_lengths[i]; j++) {
            putchar('*');
        }
        putchar('\n');
    }

    return 0;
}
