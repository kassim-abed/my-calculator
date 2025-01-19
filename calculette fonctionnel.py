import json
import time

# File to store the calculation history
history_file = "history.json"

# Calculator function
def calculator(first_value, operator, second_value):
    if operator == "+":
        return first_value + second_value
    elif operator == "-":
        return first_value - second_value
    elif operator == "*":
        return first_value * second_value
    elif operator == "/" and second_value != 0:
        return first_value / second_value
    elif operator == "//":
        return first_value // second_value
    elif operator == "%":
        return first_value % second_value
    elif operator == "**":
        return first_value ** second_value
    else:
        print("Invalid operation or division by zero.")
        return None

# Load the calculation history from the JSON file
def load_history():
    try:
        with open(history_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save the updated history back to the JSON file
def save_history(history):
    with open(history_file, "w") as file:
        json.dump(history, file, indent=4)

# Clear the history
def clear_history():
    with open(history_file, "w") as file:
        file.write("{}")  # Reset the file to an empty JSON object
    print("History cleared.")

# Main program
if __name__ == "__main__":
    history = load_history()
    
    first_value = float(input("Enter the first value: "))
    
    while True:
        user_input = input("Enter your calculation (operator value) or 'clear' to reset history: ").strip()
        
        if user_input.lower() == "clear":
            clear_history()
            history = {}
            continue
        
        try:
            operator, second_value = user_input.split()
            second_value = float(second_value)
            result = calculator(first_value, operator, second_value)
            
            if result is not None:
                # Format the operation result as a string
                operation = f"{first_value} {operator} {second_value} = {result}"
                print(f"Result: {operation}")
                
                # Add the operation to the history with a timestamp as the key
                timestamp = str(int(time.time()))
                history[timestamp] = operation
                save_history(history)
                
                first_value = result
        except ValueError:
            print("Invalid input. Use the format: operator value (e.g., + 10).")
