#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main() {
    string filename;
    cout << "Enter the name of the text file (with extension): ";
    cin >> filename;

    ifstream file(filename); // Open the file
    if (!file) {
        cout << "Error: Could not open file " << filename << endl;
        return 1;
    }

    string word;
    int wordCount = 0;

    while (file >> word) {
        wordCount++; // Count each word
    }

    file.close(); // Close the file

    cout << "The file contains " << wordCount << " words." << endl;

    return 0;
}
