"""
Filename: Functions_Investigate_2.py

Instructions:
This program demonstrates the concept of variable scope. There are two
variables named `color`: one outside the function (global scope) and one
inside the function (local scope).

Run the code and carefully observe the output.

Answer the following questions:

1. What is the value of the `color` variable *before* the function is called?
green, dictated by " color = "green" " at the start
2. What is the value of the `color` variable that is printed *from inside*
   the `change_color()` function?
blue 
3. What is the value of the `color` variable *after* the function has
   finished running?
green due to the global variable at the start not being changed
4. Why did the value of the global `color` variable not change, even though
   the function seemed to change it to "Blue"?

   The reason why this didn't change would be due to the global variable being above the local variable, therefore in order
   to change it you have to add global color to the top top of the function to effect the global variable.
"""

# This is a global variable.
color = "Green"

def change_color():
    """
    This function defines its own LOCAL variable named 'color'.
    This local variable only exists while the function is running.
    It is completely separate from the global 'color' variable.
    """
    color = "Blue" # This creates a new, local variable.
    print(f"Inside the function, the color is: {color}")

# --- Main program execution starts here ---

print(f"Before the function call, the color is: {color}")

# We call the function.
change_color()

print(f"After the function call, the color is: {color}")
