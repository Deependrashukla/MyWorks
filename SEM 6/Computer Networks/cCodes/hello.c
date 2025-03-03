#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    // Declare a pointer and initialize it to NULL
    char *x = NULL;

    // Allocate memory
    x = malloc(9);
    if (x == NULL) { // Check if memory allocation was successful
        printf("Memory allocation failed\n");
        // return 1;
    }

    // Copy a string into the allocated memory
    strcpy(x, "hello");

    // Print the string
    printf("%s\n", x+2);
    
    



    // Free the allocated memory
    free(x);

    // return 0;
}
