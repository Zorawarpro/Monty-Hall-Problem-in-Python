import random

def monty_hall_simulation(num_simulations, switch_door):
    """
    Simulate the Monty Hall problem.
    
    Parameters:
    - num_simulations: Number of simulations to run.
    - switch_door: Whether the contestant switches door after the host reveals a goat.
    
    Returns:
    - win_count: Number of wins.
    - lose_count: Number of losses.
    """
    win_count = 0
    lose_count = 0

    for _ in range(num_simulations):
        # Place a car behind one door and goats behind the other two doors
        doors = ['goat'] * 3
        car_index = random.randint(0, 2)
        doors[car_index] = 'car'

        # Contestant randomly picks a door
        contestant_choice = random.randint(0, 2)

        # Host reveals a goat behind one of the other doors
        revealed_door = random.choice([i for i in range(3) if i != contestant_choice and doors[i] == 'goat'])

        if switch_door:
            # Contestant switches to the other unchosen door
            contestant_choice = next(i for i in range(3) if i != contestant_choice and i != revealed_door)

        # Check if the contestant wins
        if doors[contestant_choice] == 'car':
            win_count += 1
        else:
            lose_count += 1

    return win_count, lose_count

# Set the number of simulations
num_simulations = 10000

# Simulate the Monty Hall problem without switching door
wins_without_switching, losses_without_switching = monty_hall_simulation(num_simulations, switch_door=False)
win_percentage_without_switching = (wins_without_switching / num_simulations) * 100
print("Without switching door:")
print(f"Number of wins: {wins_without_switching}")
print(f"Number of losses: {losses_without_switching}")
print(f"Win percentage: {win_percentage_without_switching:.2f}%")

# Simulate the Monty Hall problem with switching door
wins_with_switching, losses_with_switching = monty_hall_simulation(num_simulations, switch_door=True)
win_percentage_with_switching = (wins_with_switching / num_simulations) * 100
print("\nWith switching door:")
print(f"Number of wins: {wins_with_switching}")
print(f"Number of losses: {losses_with_switching}")
print(f"Win percentage: {win_percentage_with_switching:.2f}%")
