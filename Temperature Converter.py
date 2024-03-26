def celsius_to_fahrenheit(celsius):
  return (9 / 5 * celsius) + 32

def fahrenheit_to_celsius(fahrenheit):
  return (5 / 9 * (fahrenheit - 32))

def celsius_to_kelvin(celsius):
  return celsius + 273.15

def kelvin_to_celsius(kelvin):
  return kelvin - 273.15

def fahrenheit_to_kelvin(fahrenheit):
  return ((5 / 9) * (fahrenheit - 32)) + 273.15

def kelvin_to_fahrenheit(kelvin):
  return ((9 / 5) * (kelvin - 273.15)) + 32

def conversion(value, from_scale, to_scale):
  if from_scale.upper() == "C":
      if to_scale.upper() == "F":
          return celsius_to_fahrenheit(value)
      elif to_scale.upper() == "K":
          return celsius_to_kelvin(value)
  elif from_scale.upper() == "F":
      if to_scale.upper() == "C":
          return fahrenheit_to_celsius(value)
      elif to_scale.upper() == "K":
          return fahrenheit_to_kelvin(value)
  elif from_scale.upper() == "K":
      if to_scale.upper() == "C":
          return kelvin_to_celsius(value)
      elif to_scale.upper() == "F":
          return kelvin_to_fahrenheit(value)
  return "Invalid conversion"

# User input
value = float(input("Enter the temperature value: "))
from_scale = input("Enter the temperature scale (C for Celsius, F for Fahrenheit, K for Kelvin): ")
to_scale = input("Enter the target scale to convert (C/F/K): ")

result = conversion(value, from_scale, to_scale)
print("Converted temperature:", result)
