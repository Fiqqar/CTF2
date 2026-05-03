#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/mman.h>

char *gets(char *s);

void init() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void request_clearance() {
    char buffer[400];
    printf("Request ID: %p\n", (void*)buffer);
    puts("Submit clearance request:");
    gets(buffer);
    puts("Request submitted.");
}

int main() {
    init();
    puts("--- Enterprise Clearance Portal v3.0 ---");
    request_clearance();
    puts("Access Denied.");
    return 0;
}