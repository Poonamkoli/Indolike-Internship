#include <iostream>
using namespace std;

int main() {
    double temperature, convertedTemperature;
    char choice;

    cout << "Temperature Converter\n";
    cout << "Choose an option:\n";
    cout << "1. Celsius to Fahrenheit\n";
    cout << "2. Fahrenheit to Celsius\n";
    cout << "Enter your choice (1 or 2): ";
    cin >> choice;

    if (choice == '1') {
        cout << "Enter temperature in Celsius: ";
        cin >> temperature;
        convertedTemperature = (temperature * 9 / 5) + 32;
        cout << "Temperature in Fahrenheit: " << convertedTemperature << " °F\n";
    } else if (choice == '2') {
        cout << "Enter temperature in Fahrenheit: ";
        cin >> temperature;
        convertedTemperature = (temperature - 32) * 5 / 9;
        cout << "Temperature in Celsius: " << convertedTemperature << " °C\n";
    } else {
        cout << "Invalid choice. Please run the program again and select 1 or 2.\n";
    }

    return 0;
}
