//  print celsius to fahrenheit.

#include <stdio.h>
int main(){
    int cel;
    printf("%s %s\n", "Fahrenheit", "Celsius");
    printf("%s %s\n", "----------", "-------");
    for(cel = 0; cel <= 200; cel += 20){
        printf("%d %s %.2f\n", cel, "      ", cel*(9.0/5.0) + 32.0);
    }
    return 0;
}