import heapq
import time

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

# Goal positions for Manhattan distance
goal_pos = {}
for i, value in enumerate(GOAL):
    goal_pos[value] = (i // 3, i % 3)


class PuzzleNode:
    def __init__(self, state, parent=None, move="", g=0, h=0):
        self.state = state
        self.parent = parent
        self.move = move
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f


# -------------------------------
# Heuristic 1: Misplaced Tiles
# -------------------------------
def misplaced_tiles(state):
    count = 0
    for i in range(9):
        if state[i] != 0 and state[i] != GOAL[i]:
            count += 1
    return count


# -------------------------------
# Heuristic 2: Manhattan Distance
# -------------------------------
def manhattan_distance(state):
    distance = 0
    for i, value in enumerate(state):
        if value != 0:
            x1, y1 = i // 3, i % 3
            x2, y2 = goal_pos[value]
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance


# -------------------------------
# Generate Neighbors
# -------------------------------
def neighbors(state):
    blank = state.index(0)
    row, col = divmod(blank, 3)

    directions = [
        (-1, 0, "Up"),
        (1, 0, "Down"),
        (0, -1, "Left"),
        (0, 1, "Right")
    ]

    result = []

    for dr, dc, move in directions:
        nr = row + dr
        nc = col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            new_blank = nr * 3 + nc

            temp = list(state)
            temp[blank], temp[new_blank] = temp[new_blank], temp[blank]

            result.append((tuple(temp), move))

    return result


# -------------------------------
# Reconstruct Path
# -------------------------------
def reconstruct(node):
    path = []

    while node.parent is not None:
        path.append(node.move)
        node = node.parent

    return path[::-1]


# -------------------------------
# A* Search
# -------------------------------
def astar(start, heuristic):

    open_list = []

    heapq.heappush(
        open_list,
        PuzzleNode(start, None, "", 0, heuristic(start))
    )

    visited = set()
    expanded = 0

    while open_list:

        current = heapq.heappop(open_list)

        if current.state == GOAL:
            return reconstruct(current), expanded

        if current.state in visited:
            continue

        visited.add(current.state)
        expanded += 1

        for next_state, move in neighbors(current.state):

            if next_state not in visited:

                heapq.heappush(
                    open_list,
                    PuzzleNode(
                        next_state,
                        current,
                        move,
                        current.g + 1,
                        heuristic(next_state)
                    )
                )

    return None, expanded


# -------------------------------
# Display
# -------------------------------
def run_test(start):

    heuristics = {
        "Misplaced Tiles": misplaced_tiles,
        "Manhattan Distance": manhattan_distance
    }

    for name, func in heuristics.items():

        print("=" * 50)
        print(name)

        t1 = time.time()

        path, expanded = astar(start, func)

        t2 = time.time()

        print("Moves:", len(path))
        print("Path :", path)
        print("Nodes Expanded:", expanded)
        print("Execution Time:", round(t2 - t1, 5), "seconds")


# -------------------------------
# Example
# -------------------------------

start_state = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)

run_test(start_state)