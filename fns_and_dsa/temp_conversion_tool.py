FAHRENHEIT_TO_CELSIUS_FACTOR  = 5/9

CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
     # celcius = (f-32)*5/9
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    #  F = (9/5)*c +32
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def main():
    temperature_value = int(input("Enter the temperature to convert: "))
    temperature_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if temperature_unit == "C":
        converted_temperature = convert_to_fahrenheit(temperature_value)
        print(f"{temperature_value}°C is equal to {converted_temperature}°F")
    elif temperature_unit == "F":
        converted_temperature = convert_to_celsius(temperature_value)
        print(f"{temperature_value}°F is equal to {converted_temperature}°C")
    else:
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
