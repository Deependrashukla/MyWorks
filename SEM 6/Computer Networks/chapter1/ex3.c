// Original Program

#include <stdio.h>
int main(){
    int fahr;
    printf("%s %s\n", "Fahrenheit", "Celsius");
    printf("%s %s\n", "----------", "-------");
    for (fahr = 0; fahr <= 200; fahr += 20){
        printf("%3d %s %6.1f \n", fahr, "     ", (5.0/9.0)*(fahr-32));
    };
    return 0;
}

//  1-3. Modify the temperature conversion program to print a heading above the table

