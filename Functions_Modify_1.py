"""
Filename: Functions_Modify_1.py

Instructions:
Here is a function that prints a shipping message. Your task is to modify it
in a few steps. After each step, run the code to verify your changes.

1.  Modify the `print_shipping_message` function to accept a parameter
    called `item_name`. Inside the function, use this parameter to print
    a more specific message, like "Your shirt is on its way!". Call the
    function with an argument like "shirt" or "book".

2.  Now, change the function's name to `create_shipping_message`. Instead of
    printing the message, have the function `return` the message as a string.
    In the main part of your script, call the function, store the returned
    string in a variable, and then print that variable.

3.  (Advanced) Modify the function to accept a second parameter called
    `shipping_speed` with a default value of "standard". Use an f-string to
    include the shipping speed in the returned message, like
    "Your shirt is on its way (standard shipping)!". Call the function once
    without specifying the speed, and once with "express".
"""

# STARTING CODE
def print_shipping_message(item_name):
    """Prints a generic shipping message."""
    print(f"Your {item_name} is on its way!")

def create_shipping_message(item_name, shipping_speed="standard"):
    return (f"your {item_name} is on its way.")

def create_shipping_message(item_name, shipping_speed="standard"):
    return (f"your {item_name} is on its way ({shiping_speed} shipping).")

# --- Main program execution starts here ---
print("--- print_shipping_message with a parameter ---")
print_shipping_message("shirt")
print_shipping_message("book")

print("/n---create_shipping_message ---")
msg1 = create_shipping_message("shirt")
print(msg1)

msg2 = create_shipping_message("book", "express")
print(msg2)

msg_default = create_shipping_message("shoes")
print(msg_default)

msg_express = create_shipping_message("shoes", "express")
print(msg_express)

# --- Add your modified function calls below ---
print("\n--- Testing your modified functions ---")
# Call your modified function(s) here to test them.
