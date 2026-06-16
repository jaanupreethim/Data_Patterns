#include <stdio.h>

double power(double x, unsigned int n, int *mult_count) {
    double result = 1.0;
    *mult_count = 0;
    
    if (n == 0) return result;

    while (n > 0) {
        if (n % 2 == 1) {
            result *= x;
            (*mult_count)++;
        }
        x *= x;
        if (n > 1) { 
            (*mult_count)++;
        }
        n /= 2;
    }
    return result;
}
