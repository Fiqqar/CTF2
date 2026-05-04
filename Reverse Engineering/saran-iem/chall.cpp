#include <iostream>
#include <string>
#include <vector>

using namespace std;

void print_flag() {
    vector<int> cipher = {99, 99, 127, 116, 72, 65, 0, 69, 0, 65, 64, 90, 93, 84, 108, 93, 7, 93, 3, 108, 91, 0, 7, 87, 67, 91, 3, 93, 0, 78};
    char key = 0x33;
    
    cout << "Akses Diterima! Flag: ";
    for (int c : cipher) {
        cout << (char)(c ^ key);
    }
    cout << endl;
}

int main() {
    string input;
    cout << "=== 64 AUDIO LICENSE VALIDATOR v2.5 ===" << endl;
    cout << "Masukkan Serial Number: ";
    cin >> input;

    if (input == "iP0d_Nano_V7") {
        print_flag();
    } else {
        cout << "Lisensi Ilegal!" << endl;
    }
    return 0;
}
