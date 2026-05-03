#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

char *gets(char *s);

void init() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
}

void backdoor() {
    char flag[64];
    FILE *f = fopen("flag.txt", "r");
    if (f == NULL) {
        puts("Error: flag.txt not found.");
        exit(1);
    }
    fgets(flag, sizeof(flag), f);
    printf("Congratulations! Here is your flag: %s\n", flag);
}

void get_feedback() {
    char buffer[32];
    puts("Please leave your feedback for our developers:");
    gets(buffer); 
    puts("Thank you for your contribution.");
}

int main() {
    init();
    puts("--- Global Enterprise Feedback System v1.0 ---");
    get_feedback();
    return 0;
}
