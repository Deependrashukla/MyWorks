"""
 Modify the temperature conversion program to print the table in reverse order,
 that is, from 300 degrees to 0. 
 """

#include <stdio.h>
#include <stddef.h> // Ensure this is included
#include <stdlib.h> // Include this for good measure

int main() {
    // Print the heading with a newline character
    printf("%s %s\n", "Fahrenheit", "Celsius");

    // Print the temperature conversion table
    for (int fahr = 200; fahr >= 0; fahr -= 20) {
        printf("%3d %12.2f\n", fahr, (5.0/9.0)*(fahr - 32));
    }

    return 0;
}

