#assumption: the highest number of tickets per event = 10
#the highest price per ticket = 100
#events with zero tickets are not shown, even if they are closer

import sys
import random
from collections import defaultdict
from collections import deque
import math

class Event():
    def __init__(self, id, x, y):
        self.x = x
        self.y = y
        self.id = id
        self.tickets = [round(random.uniform(1,100),1) for _ in range(0, random.randint(0, 10))]

    def manhattan_distance(self, other_x, other_y):
        return abs(self.x - other_x) + abs(self.y - other_y)


def main(argv):
    limit = 6
    if argv:
        if argv[0] == "--all":
            limit =  math.inf

    #get user input
    user_input = input("Please Input Coordinates\n")
    try:
        coordinates_list = list(map(lambda x: int(x.strip()), user_input.split(',')))
    except ValueError:
        print("Incorrect input. Please try again.")
        return

    if len(coordinates_list) < 2:
        print("Not enough coordinates. Please try again.")
        return

    x = coordinates_list[0]
    y = coordinates_list[1]

    if not in_range(x,y):
        print("Coordinates not in rage. Please try again")
        return

    #generate seed data
    grid = seed_data()
    #get closest events
    result = get_closest_events(grid, x, y, limit=limit)
    result.sort(key=lambda x: x[1])

    count = 0
    for event, distance in result:
        if count >= 5:
            break
        print("Event {}, ${}, Distance {}".format(event.id, sorted(event.tickets)[0], distance))
        count += 1

    if limit > 6:
        print("*********All events*********")
        for event,distance in result:
            print("Event {} ({},{}), {}, Distance {}".format(event.id, event.x, event.y, sorted(event.tickets), distance))



def seed_data():
    #Generating the number of events
    number_of_events = random.randint(1,442)
    #Generating the events' coordinates
    event_set = set()

    while len(event_set) < number_of_events:
        event_set.add((random.randint(-10, 11), random.randint(-10,11)))

    #Generating the grid and events as dicts
    grid = defaultdict(dict)

    i = 0
    for x,y in event_set:
        grid[x][y] = Event(i, x, y)
        i += 1

    return grid

def not_random_seed_data():
    grid = defaultdict(dict)

    grid[-4][1] = Event(1,-4,1)
    grid[-6][5] = Event(2,-6,5)
    grid[-8][-4] = Event(3,-8,-4)
    grid[-3][-7] = Event(4,-3,-7)
    grid[2][3] = Event(5,2,3)
    grid[1][7] = Event(6,1,7)
    grid[8][0] = Event(7,8,0)
    grid[1][-1] = Event(8,1,-1)
    grid[9][-3] = Event(9,9,-3)
    grid[4][-5] = Event(10,4,-5)

    return grid

def get_closest_events(grid, starting_x, starting_y, limit=6):
    seen = set()
    closest_events = []
    queue = deque()

    queue.append((starting_x,starting_y))
    seen.add((starting_x, starting_y))

    #do a breadth-first type traversal
    while len(seen) < 441 and len(closest_events) < limit:
        if deque:
            x,y = queue.popleft()
        else:
            break

        if x in grid:
            if y in grid[x]:
                event = grid[x][y]
                if event.tickets:
                    closest_events.append((event, event.manhattan_distance(starting_x, starting_y)))

        #put all its neighbours into the queue
        if in_range(x + 1, y) and (x + 1, y) not in seen:
            queue.append((x + 1,y))
            seen.add((x + 1,y))
        if in_range(x - 1, y) and (x - 1, y) not in seen:
            queue.append((x - 1, y))
            seen.add((x - 1, y))
        if in_range(x, y + 1) and (x, y + 1) not in seen:
            queue.append((x, y + 1))
            seen.add((x, y + 1))
        if in_range(x, y - 1) and (x, y - 1) not in seen:
            queue.append((x, y - 1))
            seen.add((x, y - 1))

    return closest_events

def in_range(x, y):
    if x <= 10 and x >= -10 and y <= 10 and y >= -10:
        return True


if __name__ == "__main__":
    main(sys.argv[1:])