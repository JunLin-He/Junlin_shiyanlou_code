#include <stdio.h>

#define LOWER -30.0	//The lower of table
#define UPPER 100.0     //The upper of table
#define STEP 1.0	//The step of celsius


int main() {
    float fahr, celsius;
    float lower, upper, step;

//    lower = -30.0;
//    upper = 100.0;
//    step  = 1.0;

    celsius  = lower;

    printf("The transformation from fahr to ceisius: \n");

    for(celsius = LOWER; celsius <= UPPER; celsius += STEP) {
//        celsius = 5.0 * (fahr - 32.0) / 9.0;
	fahr = celsius * 9.0 / 5.0 + 32.0;
        printf("%3.0f\t%6.1f\n", fahr, celsius);
    }
}

