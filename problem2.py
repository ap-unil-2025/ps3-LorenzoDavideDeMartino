def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32 
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    # Your code here
    celsius = (fahrenheit - 32) * 5/9 
    return celsius 

def temperature_converter():
    """
    Interactive temperature converter.
    Ask user for:
    1. Temperature value
    2. Current unit (C or F)
    3. Convert and display result
    """
    # Your code here
    temperature = int(input("What is the temperature?"))
    unit = input("What is the current unit (C or F)?")
    if unit == "C" :
        celsius = temperature
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C or {fahrenheit}°F")
    
    elif unit == "F":
        fahrenheit = temperature 
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F or {celsius}°C")

    return celsius, fahrenheit

# Test cases (DO NOT MODIFY)
if __name__ == "__main__":
    # Test conversions
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_fahrenheit(100) == 212
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100
    print("All tests passed!")

    # Run interactive converter
    temperature_converter()