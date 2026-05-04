#include <iostream>
#include <string>
#include <sys/ptrace.h>
#include <unistd.h>
#include <vector>

using namespace std;

void anti_debug() {
    if (ptrace(PTRACE_TRACEME, 0, 1, 0) < 0) {
        exit(0);
    }
}

bool verify_license(string input) {
    if (input.length() != 12) return false;

    unsigned int acc = 0x1337;
    for (char c : input) {
        acc = (acc + (unsigned int)c) ^ 0x33;
    }

    return (acc == 0x1749);
}

void get_flag() {
    unsigned char key[] = {0x33, 0x33, 0x33, 0x33};
    unsigned char enc[] = {
        0x63, 0x63, 0x7F, 0x74, 0x48, 0x44, 0x5B, 0x07,
        0x47, 0x0C, 0x6C, 0x52, 0x6C, 0x50, 0x46, 0x40,
        0x47, 0x03, 0x5E, 0x6C, 0x45, 0x5E, 0x0C, 0x4E
    };

    for(int i = 0; i < sizeof(enc); i++) {
        printf("%c", enc[i] ^ key[i % 4]);
    }
    printf("\n");
}

int main() {
    anti_debug();

    string license;
    cout << "=== SMK RUS VAULT v4.0 (HARD) ===" << endl;
    cout << "Enter Driver License Key: ";
    cin >> license;

    if (verify_license(license)) {
        cout << "[+] Kernel Authenticated! Flag: ";
        get_flag();
    } else {
        cout << "[-] Invalid Kernel Key!" << endl;
    }
    return 0;
}