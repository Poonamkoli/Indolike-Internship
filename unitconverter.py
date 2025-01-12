def display_menu():
    print("\nUnit Converter")
    print("1. Length (Meters to Kilometers)")
    print("2. Weight (Kilograms to Pounds)")
    print("3. Temperature (Celsius to Fahrenheit)")
    print("4. Exit")

def convert_length():
    meters = float(input("Enter length in meters: "))
    kilometers = meters / 1000
    print(f"{meters} meters is {kilometers} kilometers.")

def convert_weight():
    kilograms = float(input("Enter weight in kilograms: "))
    pounds = kilograms * 2.20462
    print(f"{kilograms} kilograms is {pounds} pounds.")

def convert_temperature():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} Celsius is {fahrenheit} Fahrenheit.")

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ")

        if choice == '1':
            convert_length()
        elif choice == '2':
            convert_weight()
        elif choice == '3':
            convert_temperature()
        elif choice == '4':
            print("\nExiting Unit Converter. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
