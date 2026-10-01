# Simple Reflex Agent

def reflex_agent(location, status):
    if status == "Dirty":
        return "Clean"
    elif location == "A":
        return "Move Right"
    else:
        return "Move Left"


# Environment
environment = {
    "A": "Dirty",
    "B": "Clean"
}

location = "A"

for i in range(4):
    status = environment[location]

    print(f"\nAgent at {location}")
    print(f"Status: {status}")

    action = reflex_agent(location, status)
    print("Action:", action)

    if action == "Clean":
        environment[location] = "Clean"

    elif action == "Move Right":
        location = "B"

    elif action == "Move Left":
        location = "A"

print("\nFinal Environment:")
print(environment)