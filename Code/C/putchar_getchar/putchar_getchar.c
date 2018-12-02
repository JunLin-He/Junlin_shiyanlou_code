#include<stdio.h>

/* The program is used for copying input to output */
int main ( ) {
    int c;

    c = getchar( );
    while ( c != EOF ) {
        putchar( c );
        c = getchar ( );
    }
}

