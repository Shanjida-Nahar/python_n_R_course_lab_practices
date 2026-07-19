def temp(F):
    tempC = (tempF - 32) * 5/9
    return tempC
tempF = float(input("Enter temperature in Fahrenheit: "))
print(f"Temperature in Celsius: {temp(tempF):.2f} °C")