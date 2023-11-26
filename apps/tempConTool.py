def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def temperature_conversion_app():
    print("Temperature Conversion Tool")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = input("Choose your conversion (1/2): ")

    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C is {convert_celsius_to_fahrenheit(celsius)}°F")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F is {convert_fahrenheit_to_celsius(fahrenheit)}°C")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    temperature_conversion_app()
