#include <stdio.h>
#include "11.c"  // Include the function definition

int main() {
    const char *test_cases[] = {
        "",  // Empty Input
        "word",  // Single Word
        "This is a test.",  // Multiple Words
        "This is a test.\nThis is another test.",  // Newlines
        "This\tis\ta\ttest.",  // Tabs
        "This is a test.\nThis\tis\tanother\ttest."  // Mixed Input
    };

    const char *test_case_descriptions[] = {
        "Empty Input",
        "Single Word",
        "Multiple Words",
        "Newlines",
        "Tabs",
        "Mixed Input"
    };

    int nl, nw, nc;
    for (int i = 0; i < 6; ++i) {
        count_words(test_cases[i], &nl, &nw, &nc);
        printf("Test Case: %s\n", test_case_descriptions[i]);
        printf("Lines: %d, Words: %d, Characters: %d\n\n", nl, nw, nc);
    }

    return 0;
}


// #include <stdio.h>
// #include <assert.h>
// #include "11.c"  // Including the function to test

// void run_tests() {
//     int nl, nw, nc;
    
//     struct {
//         const char *input;
//         int expected_nl;
//         int expected_nw;
//         int expected_nc;
//     } test_cases[] = {
//         {"", 0, 0, 0},  // Empty Input
//         {"word", 0, 1, 4},  // Single Word
//         {"This is a test.", 0, 4, 15},  // Multiple Words
//         {"This is a test.\nThis is another test.", 1, 8, 35},  // Newlines
//         {"This\tis\ta\ttest.", 0, 4, 14},  // Tabs
//         {"This is a test.\nThis\tis\tanother\ttest.", 1, 8, 38}  // Mixed Input
//     };

//     for (int i = 0; i < 6; ++i) {
//         count_words(test_cases[i].input, &nl, &nw, &nc);
//         printf("Test %d: %s\n", i + 1, test_cases[i].input);
//         printf("Expected: Lines = %d, Words = %d, Characters = %d\n",
//                test_cases[i].expected_nl, test_cases[i].expected_nw, test_cases[i].expected_nc);
//         printf("Actual:   Lines = %d, Words = %d, Characters = %d\n\n", nl, nw, nc);
        
//         assert(nl == test_cases[i].expected_nl);
//         assert(nw == test_cases[i].expected_nw);
//         assert(nc == test_cases[i].expected_nc);
//     }

//     printf("All tests passed successfully!\n");
// }

// int main() {
//     run_tests();
//     return 0;
// }
