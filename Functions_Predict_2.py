"""
Filename: Functions_Predict_2.py

Instructions:
Read the code below. Pay close attention to the variables `team_score`
and the parameter `points_to_add`.

Without running the code, predict the final output. What will the two print
statements display? Write down your prediction and your reasoning.
"""
The final output will be
before calling the function the team score will be 100 because of the global variable
The print of 100 is then displayed
Then inside the function the score becomes 60 after adding the local variable of 50 + 10 from the calculate_new_score variable
being set to 10. Then it prints the final_score as 60.
Finally, the team_score will still be 100 because nothing was ever put in to affect the global variable
"""
# A global variable, accessible everywhere in this file.
team_score = 100

def calculate_new_score(points_to_add):
    """
    This function calculates a new score but doesn't change the global
    team_score. It returns the new calculated score.
    """
    # 'team_score' inside this function is a NEW, LOCAL variable.
    # It is different from the global one.
    team_score = 50
    new_score = team_score + points_to_add
    print(f"Inside the function, the score is: {new_score}")
    return new_score

# Main part of the program
print(f"Before calling the function, the team score is: {team_score}")

# We call the function and store its return value
final_score = calculate_new_score(10)

print(f"After calling the function, the team score is still: {team_score}")
