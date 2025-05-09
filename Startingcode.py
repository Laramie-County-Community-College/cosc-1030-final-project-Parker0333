import random

def three_point_strategy(three_pt_percent, three_win_count, three_total_points):
    success = random.random() < three_pt_percent
    if success:
        points = 3
        three_win_count = three_win_count + 1
    else:
        points = 0
    three_total_points = three_total_points + points
    return three_win_count, three_total_points

def two_point_strategy(two_pt_percent, free_throw_percent, two_win_count, two_total_points):
    success = random.random() < two_pt_percent
    if success:
        points = 2
    else:
        points = 0
    opponent_points = 0
    if random.random() < free_throw_percent:
        opponent_points = opponent_points + 1
    if random.random() < free_throw_percent:
        opponent_points = opponent_points + 1
    if points > 0:
        two_win_count = two_win_count + 1
    extra = opponent_points * 2
    two_total_points = two_total_points + points + extra
    return two_win_count, two_total_points

def simulate(trials, three_p, two_p, ft):
    three_win_count = 0
    three_total_points = 0
    two_win_count = 0
    two_total_points = 0

    count = 0
    while count < trials:
        three_win_count, three_total_points = three_point_strategy(three_p, three_win_count, three_total_points)
        two_win_count, two_total_points = two_point_strategy(two_p, ft, two_win_count, two_total_points)
        count = count + 1

    three_win_rate = (three_win_count / trials) * 100
    three_avg_points = three_total_points / trials
    two_win_rate = (two_win_count / trials) * 100
    two_avg_points = two_total_points / trials

    return three_win_rate, three_avg_points, two_win_rate, two_avg_points

start = input("Enter 'start' when you are ready to begin, or enter 'help' for assistance with the simulation: ").lower()

if start == "help":
    print("This is a Monte Carlo simulation, you will insert values listed below to determine the best steps to take for you to win your basketball game.\nYour three pointer percentage is the percentage of three pointers your player makes, for example if you shot four three pointers, and made one, your three pointer percentage is 25.\nYour two pointer percentage is the percentage of two pointers your player makes, for example if you shoot three two pointers, and make one, your two pointer percentage is 33.\nYour opponents free throw percentage is the percentage of three throws that they make, for example if they shot two free throws and made one, their free throw percentage is 50.\nTime left should be converted to seconds, this can be done by multiplying the minutes by 60, then adding the seconds onto it, for example 3 minutes and 20 seconds is 200 seconds.\nHappy simulating!")
elif start == "start":
    three_p = float(input("3-point percentage (1-100): "))
    three_p = three_p / 100
    two_p = float(input("2-point percentage (1-100): "))
    two_p = two_p / 100
    ft = float(input("Opponent's free throw percentage (1-100): "))
    ft = ft / 100
    trials = 10000

    three_win_rate, three_avg_points, two_win_rate, two_avg_points = simulate(trials, three_p, two_p, ft)
    print("3-Point success rate:")
    print(three_win_rate)
    print("3-Point average points:")
    print(three_avg_points)
    print("2-Point success rate:")
    print(two_win_rate)
    print("2-Point average points:")
    print(two_avg_points)
else:
    print("Invalid input, please restart simulation.")