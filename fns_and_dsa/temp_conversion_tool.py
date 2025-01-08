FAHRENHEIT_TO_CELSIUS_FACTOR  = 5/9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def main():
    temperature_value = int(input("Enter the temperature to convert: "))
    temperature_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()

    if temperature_unit == "c":
        converted_temperature = convert_to_fahrenheit(temperature_value)
        print(f"{temperature_value}°C is equal to {converted_temperature}°F")
    elif temperature_unit == "f":
        converted_temperature = convert_to_celsius(temperature_value)
        print(f"{temperature_value}°F is equal to {converted_temperature}°C")
    else:
        print("Invalid temperature unit. Please enter C for Celsius or F for Fahrenheit.")

if __name__ == "__main__":
    main()
