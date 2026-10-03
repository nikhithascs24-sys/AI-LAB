

def display(state):
    print("-------------")
    for i in range(0, 9, 3):
        print("|", state[i], "|", state[i + 1], "|", state[i + 2], "|")
    print("-------------")


def get_neighbors(state):
    neighbors = []

 
    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    
    moves = [
        (-1, 0),   
        (1, 0),    
        (0, -1),   
        (0, 1)    
    ]

    for dr, dc in moves:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_blank = new_row * 3 + new_col

         
            new_state = list(state)

           
            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            neighbors.append(tuple(new_state))

    return neighbors


def dfs(initial, goal):

    
    stack = [(initial, [initial])]

   

    while stack:

       
        current, path = stack.pop()

        if current == goal:
            return path

    
        if current in visited:
            continue

        visited.add(current)

        neighbors = get_neighbors(current)

        for neighbor in neighbors:

            if neighbor not in visited:
                stack.append(
                    (neighbor, path + [neighbor])
                )

    return None




initial = (
    1, 2, 3,
    5, 6, 0,
    4, 7, 8
)

goal = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

print("INITIAL STATE:")
display(initial)

print("GOAL STATE:")
display(goal)

solution = dfs(initial, goal)

if solution:

    print("\nDFS SOLUTION FOUND")
    print("Number of moves:", len(solution) - 1)

    print("\nSolution Path:")

    for step, state in enumerate(solution):

        print("\nStep", step)
        display(state)

else:
    print("No solution found.")
