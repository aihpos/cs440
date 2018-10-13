import random


class Node(object):
    def __init__(self, node_id = None, visited = False, parent_node_id = None,  ctc = None, neighbors = [], id_cost = []):
        self.id = node_id
        self.vis = visited 
        self.parent = parent_node_id
        self.ctc = ctc
        self.neighbors = neighbors 
        self.id_cost = id_cost 


class Queue:
#    from collections import deque
    def __init__ (self):
        self.values =[]

    def isEmpty(self):
        if not self.values:
            return True
        return false

    def enqueue(self, node):
        self.values.insert(0, node)
        #self.values.

    def dequeue(self):
        return self.values.pop(0)

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For Search Algorithms 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''

# comment out later - trying to figure out how graph is defined
    #graph[n] = [node_id, visited, parent after CTC final, CTC, neighbors, id-cost-tuple]
'''
    _graph[1] = [1, False, 0, 0, 7, [(2, 1), (3, 4)], {2:1, 3:4}]
    _graph[2] = [2, False, 0, 0, 6, [(3, 2), (4, 5), (5, 12)], {3:2, 4:5, 5:12}]
    _graph[3] = [3, False, 0, 0, 4, [(4, 2)], {4:2}]
    _graph[4] = [4, False, 0, 0, 2, [(5, 3)], {5:3}]
    _graph[5] = [5, False, 0, 0, 0, [], {}]

'''
'''
BFS add to queue 
'''
# i'm figuring out how to implement Queue as a LL bc the nodes in it need to have all those properties

queue_BFS = Queue()
queue_DFS = Queue()
queue_UC = Queue()
queue_ASTAR = Queue()


def add_to_queue_BFS(node_id, parent_node_id, cost, initialize=False):
    # Your code here
     return

'''
BFS add to queue 
'''
def is_queue_empty_BFS():
    # Your code here
    if not queue_BFS:
        return True #need to define queue_BFS as a global variable
    return False

'''
BFS pop from queue
'''
def pop_front_BFS():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    return (node_id, parent_node_id)
'''
********************************************************************************************part2: 
'''
'''
DFS add to queue 
'''
def add_to_queue_DFS(node_id, parent_node_id, cost, initialize=False):
    dfs_node = Node()
    dfs_node.id = node_id
    dfs_node.parent = parent_node_id
    dfs_node.ctc = cost
    dfs_node.vis = initialize #not sure if visited is the best name for this

    #print("adding these values to queue", dfs_node.id)
    queue_DFS.enqueue(dfs_node)
    # Your code here
    return

'''
DFS add to queue 
'''
def is_queue_empty_DFS():
    # Your code here
    if not queue_DFS:
        return True #need to define queue_DFS as a global variable
    return False

'''
DFS pop from queue
'''
def pop_front_DFS():
    (node_id, parent_node_id) = (0, 0) #what is this?
    # Your code here
    deq_node = queue_DFS.dequeue() #need to dequeue a node, not an integer
    #print("deq node is: ", deq_node)
    (node_id, parent_node_id) = (deq_node.id, deq_node.parent)
    return (node_id, parent_node_id)
'''
********************************************************************************************part2: 

'''
'''
UC add to queue 
'''
def add_to_queue_UC(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    return

'''
UC add to queue 
'''
def is_queue_empty_UC():
    # Your code here
    if not queue_UC:
        return True #need to define queue_UC as a global variable
    return False

'''
UC pop from queue
'''
def pop_front_UC():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    return (node_id, parent_node_id)

'''
A* add to queue 
'''
def add_to_queue_ASTAR(node_id, parent_node_id, cost, initialize=False):
    # Your code here
    return

'''
A* add to queue 
'''
def is_queue_empty_ASTAR():
    # Your code here
    if not queue_ASTAR:
        return True #need to define queue as a global variable
    return False

'''
A* pop from queue
'''
def pop_front_ASTAR():
    (node_id, parent_node_id) = (0, 0)
    # Your code here
    return (node_id, parent_node_id)

''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''
'''
                For n-queens problem 
'''
''' ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ '''


'''
Compute a random state 
'''
def get_random_state(n):
    state = []
    # Your code here
    state = []
    for i in range(n):  # creates list from 0 to n-1
        state.append(random.randint(1, n))
    return state

'''
Compute pairs of queens in conflict 
'''
def compute_attacking_pairs(state):
    #print('Current state', state, 'length', len(state))
    number_attacking_pairs = 0
    # existing_els = [] # occupied spots

    for j in range(0, len(state)):
        # iterates through every queen
        for i in range(0, len(state)):
            # iterates through every spot for every queen
            if (state[i] == state[j]) & (i != j):
                # found horizontal match
                number_attacking_pairs += 1

            # checks if 2 queens share a diagonal
            rowdiff = abs(state[i] - state[j])
            coldiff = abs(i - j)
            # print('rowdiff ', rowdiff)
            # print('coldiff ', coldiff)

            if (rowdiff == coldiff) & (i != j):
                number_attacking_pairs += 1

    number_attacking_pairs = number_attacking_pairs / 2
    return number_attacking_pairs

'''
The basic hill-climing algorithm for n queens
'''
def hill_desending_n_queens(state, comp_att_pairs):
    final_state = []
    # Your code here

    # initializes 2d matrix representing chessboard
    n = len(state)
    chessboard = [[0 for i in range(n)] for j in range(n)]
    minvalue = n*n
    minvalue_prev = n-1

    while minvalue != 0:
        minvalue = n*n
        minvalue_i = n-1
        minvalue_j = n-1
        state = copy.copy(state)
        tempstate = copy.copy(state)

        for i in range(0,n):
            # calculates all attacking pairs for each spot on board
            # fills in chessboard with obj func values
            for j in range(0,n):
                tempstate[i] = j + 1
                chessboard[i][j] = comp_att_pairs(tempstate)

                # save the minimum value
                if chessboard[i][j] < minvalue:
                    # store value and location
                    # this method ensures the leftmost, uppermost queen is moved if there are ties
                    minvalue_i = i
                    minvalue_j = j
                    minvalue = chessboard[i][j]
            # reset state value
            tempstate = copy.copy(state)
        # print('chessboard')
        # print(chessboard)
        # after finding the min value and target move, changes the state
        # print('minvalue_i: ', minvalue_i)
        state[minvalue_i] = minvalue_j + 1
        # print('state:')
        # print(state)

        if minvalue == minvalue_prev:
            # same values, throw error and break
            # print('error same minvalue')
            break

        minvalue_prev = copy.copy(minvalue)

    final_state = copy.copy(state)
    # print(final_state)
    return final_state

'''
Hill-climing algorithm for n queens with restart
'''
def n_queens(n, get_rand_st, comp_att_pairs, hill_descending):
    final_state = []
    # Your code here

    # generates first random state
    state = get_rand_st(n)
    # computes initial attacking pairs
    attacking_pairs = copy.copy(comp_att_pairs(state))

    # runs hill descending algorithm
    final_state = copy.copy(hill_descending(state, comp_att_pairs))

    while attacking_pairs != 0:
        # random restart
        # generates first random state
        state = get_rand_st(n)
        # computes initial attacking pairs
        attacking_pairs = copy.copy(comp_att_pairs(state))

        # runs hill descending algorithm
        final_state = copy.copy(hill_descending(state, comp_att_pairs))
        attacking_pairs = compute_attacking_pairs(final_state)

    return final_state
