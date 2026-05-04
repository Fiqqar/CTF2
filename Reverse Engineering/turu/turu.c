#include <stdio.h>
#include <unistd.h>

int main() {
	volatile unsigned int auth_sleep = 10800;
    unsigned char key[] = {0x77, 0x61, 0x69, 0x74};
    unsigned char enc[] = {
        0x27, 0x31, 0x25, 0x33, 0x0C, 0x11, 0x5D, 0x00,
        0x46, 0x04, 0x07, 0x17, 0x44, 0x3E, 0x58, 0x07,
        0x28, 0x55, 0x36, 0x02, 0x46, 0x13, 0x1D, 0x01,
        0x44, 0x3E, 0x0B, 0x01, 0x03, 0x3E, 0x01, 0x47,
        0x0F, 0x3E, 0x58, 0x07, 0x28, 0x07, 0x5D, 0x07,
        0x03, 0x52, 0x1B, 0x09
    };

    printf("==========================================\n");
    printf("   DATABASE SMK RADEN UMAR SAID - VAULT v1.0   \n");
    printf("==========================================\n");
    printf("[*] Sistem sedang memverifikasi identitas...\n");
    printf("[*] Mohon tunggu proses autentikasi.\n");
    fflush(stdout);

    sleep(auth_sleep);

    printf("\n[+] VERIFIKASI SELESAI!\n");
    printf("[+] FLAG: ");
    int len = sizeof(enc);
    for (int i = 0; i < len; i++) {
        printf("%c", enc[i] ^ key[i % 4]);
    }
    printf("\n");
    return 0;
}
