#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *gets(char *s);

void init() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
}

void verify_session() {
    char buffer[64];
    puts("Enter Session Token:");
    gets(buffer);
}

int main() {
    init();
    puts("--- Enterprise Session Manager ---");
    verify_session();
    puts("Access Denied.");
    return 0;
}
