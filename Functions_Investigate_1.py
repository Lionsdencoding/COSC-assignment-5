"""
Filename: Functions_Investigate_1.py

Instructions:
This program calculates the area of a circle. It is broken down into two
functions. Run the code and observe the output.

Answer the following questions in your own words:

1. What is the purpose of the `get_radius_from_user()` function? What value
   does it `return`?
The purpose of the function is to prompt the use to enter their radius, convert that value to a float value,
then return the float value
2. What is the purpose of the `calculate_area(radius)` function? What is the
   `radius` variable in this function called (an argument or a parameter)?
the purpose of `calculate_area(radius)' is to compute the area following the formula pi * r^2 and then print the result.
The readius variable is a parameter.
3. In the main part of the program, a variable named `user_radius` is created.
   How is its value used in the call to `calculate_area`?
this value is used to store the value gotten from "get_radius_from_user()". Then after the value is gotten it is
passed on to `calculate_area' as a argument making it `calculate_area(radius)` with the value filling in the radius portion.
4. Trace the flow of the program. Which function is called first? After that
   function finishes, what happens next?
   1. The first function called is "get_radius_from_user()" which prints a prompt, waits for input, converts the input
   to a float, then returns it.

   2. The second function that get called upon is "user_radius" which gets called upon to store the value from "get_radius_from_user()"

   3. The next function called is "calculate_area(User_radius)" which calculates the radius following the value being stored in "user_radius"
   and using it in the formula pi * r^2

   4. The fourth and final function that gets called is "calculate_area" which then does the formula and finally prints it within the prompt given. 
"""

import math # We need this for the value of pi

def get_radius_from_user():
    """Asks the user for a radius and returns it as a float."""
    print("Let's calculate the area of a circle.")
    radius_input = float(input("Please enter the radius: "))
    return radius_input

def calculate_area(radius):
    """Takes a radius as a parameter and prints the area."""
    # The formula for the area of a circle is pi * r^2
    area = math.pi * (radius ** 2)
    print(f"A circle with a radius of {radius} has an area of {area:.2f}.")


# --- Main program execution starts here ---

# First, we get the radius from the user and store it.
user_radius = get_radius_from_user()

# Then, we pass that stored radius into our calculation function.
calculate_area(user_radius)
