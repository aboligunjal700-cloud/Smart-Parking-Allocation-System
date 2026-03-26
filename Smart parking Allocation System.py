from collections import deque

print("===== Smart Parking Allocation System =====")

print("Details:")
serial_no = int(input("Enter serial_no:"))
car_num = input("car_num:")
owner_num = int(input("owner_num:"))
park_hrs = int(input("park_hrs:"))
Charges = (park_hrs * 30)
print("Charges:", Charges )

parking = [
    ['E', '0', 'X', '0'],
    ['X', 'X', 'X', 'X'],
    ['0', '0', '0', 'X']
]

rows = len(parking)
cols = len(parking[0])

# Find entry point
for i in range(rows):
    for j in range(cols):
        if parking[i][j] == 'E':
            start = (i, j)

# Directions with names
directions = [
    (-1, 0, "UP"),
    (1, 0, "DOWN"),
    (0, -1, "LEFT"),
    (0, 1, "RIGHT")
]

# BFS
queue = deque()
queue.append((start[0], start[1], []))  # path list

visited = set()
visited.add(start)

found = False

while queue:
    r, c, path = queue.popleft()

    # If empty slot found
    if parking[r][c] == '0':
        print(f"\nNearest Slot Found at: ({r},{c})")
        print("Car Movement Path:")
        
        if not path:
            print("Already at parking slot!")
        else:
            for step in path:
                print(step, end=" → ")
            print("PARKED 🚗")

        found = True
        break

    for dr, dc, move in directions: #dr=change in row,dc=change in column
        nr = r + dr  #nr = new row
        nc = c + dc  #nc = new column

        if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
            if parking[nr][nc] != 'X':
                queue.append((nr, nc, path + [move]))
                visited.add((nr, nc))

if not found:
    print("No parking slot available!")
