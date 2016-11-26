from Queue import PriorityQueue
from board import Board
import math

def construct_path(start_tile, goal_tile):
    """
    Construct a path using the a star algorithm
    Returns a path list of (x, y), unreversed, doesn't include start.
    
    start_tile and goal_tile are of Tile class.
    """
    if start_tile == goal_tile:
        return [start_tile]
    frontier = PriorityQueue()
    frontier.put((0, start_tile))
    came_from = {}
    came_from[start_tile] = None
    cost_so_far = {}
    cost_so_far[start_tile] = 0
    
    while not frontier.empty():
        current = frontier.get()[1]
        print("Expanding: {}, {}".format(current.x, current.y))
        
        if current == goal_tile:
            break
        
        for next in current.get_neighbors():
            new_cost = cost_so_far[current] + next.cost
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + manhattan_distance((goal_tile.x, goal_tile.y), (next.x, next.y))
                print("Priority: {}, {}: {}".format(next.x, next.y, priority))
                frontier.put((priority, next))
                came_from[next] = current
            
    current = goal_tile
    path = [current]
    while current != start_tile:
        current = came_from[current]
        path.append(current)
    path.pop()  # Remove the starting node.
    return path
            
def manhattan_distance(a, b):
   # Manhattan distance on a square grid
   return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)