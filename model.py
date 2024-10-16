import csv

def check_odd_even(number):
    if number % 2 == 0:
        return f"{number} is even."
    else:
        return f"{number} is odd."

def validate_input(input_value):
    if not input_value:
        return {"is_valid": False, "error_message": "Input cannot be empty"}
    
    try:
        number = int(input_value)
        if number < 0:
            return {"is_valid": False, "error_message": "Number must be positive"}
    except ValueError:
        return {"is_valid": False, "error_message": "Invalid input, must be an integer"}
    
    return {"is_valid": True, "error_message": None}

def store_data(number, result):
    with open("data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([number, result])

def store_error(input_value, error_message):
    with open("data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([input_value, error_message])
