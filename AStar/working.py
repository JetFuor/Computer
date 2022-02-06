
print("A* Implementation in Python:\n")

"""
    Perform A* Traversal and find the optimal path to reach goal
    Args:
        Cost: Cost matrix (list of floats/int)
        Heuristic: Heeuristics for A* (list of floats/int)
        Start_point: Starting node (int)
        Goals: Goal states (list of ints)
    Returns:
        Path: Path to goal state obtained from A* (list of ints)
"""

# Taking value from heuristic and path_len only used 
def f(g, h, n): 
    return g[n] + h[n]

# Removing from a list and adding to another, value m
def update(list_remove, list_add, m):
    list_remove.remove(m)
    list_add.append(m)

# Main function
def a_star_imp(cost, heuristic, start, goals):
    pathSet = []

    open_list = [start] # Keeps track of unvisited nodes
    closed_list = [] # Keeps track of visited nodes

    path_len = {} # Contain length of the path so far for each node
    path_len[start] = 0

    # Showing the node that need to go through to get to it
    parent_nodes = {}
    parent_nodes[start] = start

    # Goes through entire open_list
    while len(open_list) > 0:
        node = None

        # Goes through the open_list, nodes one by one, finding one with shortest path from current node
        for n in open_list:
            if node == None or f(path_len, heuristic, n) < f(path_len, heuristic, node): # n is the first node, just start program or current node f less than previous node f
                # Chooses node with the shortest path from the current node
                node = n # New n is node
        
        if node == None:
            #No path exists
            break

        if node in goals: # See if reached the goal
            # Calculates the f value for this node
            fv_n = f(path_len, heuristic, node)
            reconstruct = []

            aux = node
            # Finding the pathing to the end node, by reversing the process
            while parent_nodes[aux] != aux: # Traversing a linked list, [(S, 9, S), (A, 6, S)], A is aux, S is parent
                reconstruct.append(aux) # [A, ], then moves on to S
                aux = parent_nodes[aux]

            reconstruct.append(aux) # [A, B, C, S], want path from start to end
            reconstruct.reverse() # Makes it end to start

            # Putting it all into another node instead
            pathSet.append( (reconstruct, fv_n) )

            update(open_list, closed_list, node)
            continue

        # Getting the node and its costing
        path_cost = cost[node] #2 -> [0, -1, 0, 3, -1, -1, 9, -1, -1, -1, -1]

        # Searching for the paths and updating the costs
        for index in range(0, len(path_cost)):
            # Starts with path
            weight = path_cost[index]

            # Skips all the none paths
            if weight > 0:
                # See if it has been visited before, if not go here
                if index not in open_list and index not in closed_list:
                    # Show where we at
                    open_list.append(index)
                    parent_nodes[index] = node
                    # Showing the path cost currently
                    path_len[index] = path_len[node] + weight

                else:
                    # If it has been visited before, goes here
                    if path_len[index] > path_len[node] + weight: 
                        # Seeing if the weight needs to be updated or not, is there a shorter path to this place
                        path_len[index] = path_len[node] + weight
                        parent_nodes[index] = node

                        if index in closed_list:
                            update(closed_list, open_list, index)


        update(open_list, closed_list, node)

    #pathSet [ ([], 12), ([], 8), ... ] 8 is the f value
    # If a path is found
    if len(pathSet) > 0:
        pathSet = sorted(pathSet, key=lambda x: x[1]) # Sorts it smallest to largest
        path = pathSet[0][0]
    else:
        path = []

    return path

'''
Driver code
'''
# 0 Means no path there
# The numbers are the cost to go to the nodes in there, so for node 1 it cost 5 to go to node 2
give_cost = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #0
            [0, 0, 5, 9, 0, 6, 0, 0, 0, 0, 0], #1
            [0, 0, 0, 3, 0, 0, 9, 0, 0, 0, 0], #2
            [0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 0], #3
            [0, 6, 0, 0, 0, 0, 0, 5, 7, 0, 0], #4
            [0, 0, 0, 0, 2, 0, 0, 0, 0, 2, 0], #5
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #6
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #7
            [0, 0, 0, 0, 0, 2, 0, 0, 0, 0, 8], #8
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7], #9
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] #10

start = 1
give_goals = [7]
heuristic = [0, 5, 7, 3, 4, 6, 0, 0, 6, 5, 0] # Hard coded for now

getPath = a_star_imp(give_cost, heuristic, start, give_goals)

print(getPath) 
# 6 -> [1, 2, 6]
# 7 -> [1, 5, 4, 7]