#include <stdio.h>
#include <stdlib.h>

int fib(int n) {
    if (n <= 1) {
        return n;
    }
    long long int result = (fib(n-1) + fib(n-2));
    return result;
}

int main() {
    for (int i = 0; i < 1000; i++) {
        printf("%d", fib(i));
        printf("\n");
    }
}
