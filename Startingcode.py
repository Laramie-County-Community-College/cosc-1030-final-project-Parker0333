import random
def three_point_strat
def two_point_strat
Simulation_start = input("Welcome to the Monte Carlo simulation, enter 'Start' when you are ready to begin, or enter 'Help' for assistance with the simulation.")
if Simulation_start.lower() == "start":
    #User inputed variables used in the functions
    Three_p_percent = (input("Please insert a numerical value 1 to 100 for your three pointer percentage."))
    Two_p_percent = (input("Please insert a numerical value 1 to 100 for your two pointer percentage."))
    opponents_Fthrow = (input("Please insert a numerical value 1 to 100 for your opponents free throw percentage."))
    Time = (input("Please insert a numerical value for the time remaining in the game in seconds."))
#Help statement to assist confused users
if Simulation_start.lower() == "help":
    print("This is a Monte Carlo simulation, you will insert values listed below to determine the best steps to take for you to win your basketball game.\nYour three pointer percentage is the percentage of three pointers your player makes, for example if you shot four three pointers, and made one, your three pointer percentage is 25.\nYour two pointer percentage is the percentage of two pointers your player makes, for example if you shoot three two pointers, and make one, your two pointer percentage is 33.\nYour opponents free throw percentage is the percentage of three throws that they make, for example if they shot two free throws and made one, their free throw percentage is 50.\nTime left should be converted to seconds, this can be done by multiplying the minutes by 60, then adding the seconds onto it, for example 3 minutes and 20 seconds is 200 seconds.\nHappy simulating!")

else:
    print("No start test")
    