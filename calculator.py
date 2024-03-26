sr = input("Enter Type Of Math:")
sn1 = input("Enter A Number: ")
sn2 = input("Enter Another Number:")
sf1 = float(sn1)
sf2 = float(sn2)

def calculator(number1, number2):
    try:
        if sr == "math":
            result = number1 + number2
        elif sr == "sub":
            result = number1 - number2
        elif sr == "mult":
            result = number1 * number2
        elif sr == "div":
            result = number1 / number2
        elif sr == "rem":
            result = number1 % number2
        elif sr == "intd":
            result = number1 // number2
        elif sr == "Expo":
            result = number1 ** number2
        else:
            print("Error: Invalid operation")
            return None  # Return None if operation is invalid
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None  # Return None if division by zero occurs
    except ValueError:
        print("Error: Invalid input")
        return None  # Return None if input is not a number

ans = calculator(sf1, sf2)

if ans is not None:
    print("The Answer is:", ans)
