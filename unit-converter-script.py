def temperature_conversion(value, from_unit, to_unit):
    if from_unit == "celsius" and to_unit == "fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "fahrenheit" and to_unit == "celsius":
        return (value - 32) * 5/9
    elif from_unit == to_unit:
        return value
    else:
        return None

def length_conversion(value, from_unit, to_unit):
    # Conversion factors to meters
    units = {
        "meter": 1,
        "kilometer": 1000,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "inch": 0.0254,
        "foot": 0.3048,
        "yard": 0.9144,
        "mile": 1609.34
    }
    if from_unit in units and to_unit in units:
        return value * units[from_unit] / units[to_unit]
    else:
        return None

def mass_conversion(value, from_unit, to_unit):
    # Conversion factors to grams
    units = {
        "gram": 1,
        "kilogram": 1000,
        "milligram": 0.001,
        "pound": 453.592,
        "ounce": 28.3495
    }
    if from_unit in units and to_unit in units:
        return value * units[from_unit] / units[to_unit]
    else:
        return None

def time_conversion(value, from_unit, to_unit):
    # Conversion factors to seconds
    units = {
        "second": 1,
        "minute": 60,
        "hour": 3600,
        "day": 86400,
        "week": 604800
    }
    if from_unit in units and to_unit in units:
        return value * units[from_unit] / units[to_unit]
    else:
        return None

def unit_converter():
    print("Unit Converter")
    print("Supported conversions: Temperature, Length, Mass, Time")

    unit_type = input("Enter the type of unit to convert (temperature/length/mass/time): ").lower()
    from_unit = input("Enter the unit to convert from: ").lower()
    to_unit = input("Enter the unit to convert to: ").lower()
    value = float(input("Enter the value to convert: "))

    result = None

    if unit_type == "temperature":
        result = temperature_conversion(value, from_unit, to_unit)
    elif unit_type == "length":
        result = length_conversion(value, from_unit, to_unit)
    elif unit_type == "mass":
        result = mass_conversion(value, from_unit, to_unit)
    elif unit_type == "time":
        result = time_conversion(value, from_unit, to_unit)

    if result is not None:
        print(f"{value} {from_unit} is equal to {result} {to_unit}")
    else:
        print("Invalid conversion or units. Please check your input and try again.")

if __name__ == "__main__":
    unit_converter()
