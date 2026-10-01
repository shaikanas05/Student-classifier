# Goal-Based Agent

goal = 5
position = 0

while position != goal:
    print("Current Position:", position)

    if position < goal:
        action = "Move Forward"
        position += 1
    else:
        action = "Move Backward"
        position -= 1

    print("Action:", action)

print("\nGoal Reached!")
print("Final Position:", position)