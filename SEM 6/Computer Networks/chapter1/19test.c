#include <stdio.h>
#include <string.h>
#include <assert.h>

#define MAX_LINE 1000  // Maximum line length

// Function prototypes
void reverse(char s[]);
int get_line(char s[], int limit);

// Test function for reverse()
void test_reverse() {
    char str1[] = "hello";
    reverse(str1);
    assert(strcmp(str1, "olleh") == 0);

    char str2[] = "abcd";
    reverse(str2);
    assert(strcmp(str2, "dcba") == 0);

    char str3[] = "";
    reverse(str3);
    assert(strcmp(str3, "") == 0);

    char str4[] = "a";
    reverse(str4);
    assert(strcmp(str4, "a") == 0);

    printf("All reverse() tests passed!\n");
}

// Test function for get_line()
void test_get_line() {
    char buffer[MAX_LINE];

    // Redirect stdin to read from a file
    freopen("test_input.txt", "r", stdin);

    // Test reading the first line
    assert(get_line(buffer, MAX_LINE) > 0);
    assert(strcmp(buffer, "Hello\n") == 0);

    // Test reading the second line
    assert(get_line(buffer, MAX_LINE) > 0);
    assert(strcmp(buffer, "World\n") == 0);

    printf("All get_line() tests passed!\n");
}

// Main function to run all tests
int main() {
    test_reverse();
    test_get_line();
    printf("All tests passed successfully!\n");
    return 0;
}