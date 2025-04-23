def fahrenheit_to_celsius():
    fahrenheit_temps = [random.randint(32, 100) for _ in range(5)]
    celsius_temps = [(temp - 32) * 5 / 9 for temp in fahrenheit_temps]
    print(f"Fahrenheit temperatures: {fahrenheit_temps}")
    print(f"Converted Celsius temperatures: {celsius_temps}")
