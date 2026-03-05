from collections import deque

def water_jug():

    visited = set()

    queue = deque([(0,0)])

    while queue:

        x,y = queue.popleft()

        if (x,y) in visited:
            continue

        visited.add((x,y))

        print(x,y)

        if x == 4:
            print("Goal reached!")
            return

        queue.append((5,y))
        queue.append((x,3))
        queue.append((0,y))
        queue.append((x,0))

        transfer = min(x,3-y)
        queue.append((x-transfer, y+transfer))

        transfer = min(y,5-x)
        queue.append((x+transfer, y-transfer))


water_jug()