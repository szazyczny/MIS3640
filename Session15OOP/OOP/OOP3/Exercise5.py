# Exercise 5 (group work)
# Write a definition for a class of anything you want. You have to use the following methods:

# __init__ method that initializes some attributes. One of the attributes has to be an empty list.

# __str__ method that returns a string that reasonably represent the thing.

# A special method that overloads the one type of operators.

# Some other methods that reasonably represent the thing's actions, inclduing one method that takes an object of any type and adds it to the attribute of type list.

# Test your code by creating two objects and using all the methods.

# https://docs.python.org/3/tutorial/classes.html#class-and-instance-variables

class Exercise:
    """
    Represents the list of exercises.

    attributes: muscle, exercise
    """

    def __init__(self, muscle):
        self.muscle = muscle
        self.exercises = []    # creates a new empty list for each dog

    def add_exercise(self, exercise):
        self.exercises.append(exercise)

core = Exercise('Core')
upper = Exercise('Upper')
lower = Exercise('Lower')

core.add_exercise('Crunch')
upper.add_exercise('Push Up')
lower.add_exercise('Squat')

# core.exercise
# upper.exercise
# lower.exercise