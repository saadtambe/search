# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

#     stack = util.Stack()
#     for child_node in problem.getSuccessors(problem.getStartState()):
#         stack.push(child_node)
#     move_list = []
#     visited = []
#     
#     def DFS_step():
#         
#         node = stack.pop() #node popped at this step of DFS, add to visited and find children if any and add to stack
#         visited.append(node)
#         move_list.append(node)
#         print "current node: ",node 
#         if problem.isGoalState(node[0]):
#             return move_list
#         
#         if problem.getSuccessors(node[0]):
#             
#             for child_node in problem.getSuccessors(node[0]): #maybe do some list comp here to list in Depth-first order
#                 if child_node not in visited:
#                     stack.push(child_node)
#                     end_of_line = DFS_step()
#                     if end_of_line == False:
#                         move_list.pop()
#                         #so much memory waste
#         else:
#             return False
#         
#         
#     DFS_step()
#     
    
    
#     stack = util.Stack()
#     visited = []
#     move_list = []
#     if problem.isGoalState(problem.getStartState()):
#         return move_list
#     
#     visited.append(problem.getStartState())
# 
#     for child_node in list(reversed(problem.getSuccessors(problem.getStartState()))): #list comp here to reverse the successors. order of successors goes NORTH > SOUTH > EAST > WEST
#         stack.push(child_node)
#         
#     while not stack.isEmpty():
#         node = stack.pop()
#         if problem.isGoalState(node):
#             return move_list
#         print "current node: ",node
#         if node[0] not in visited:
#             visited.append(node[0])
#             #let your hair grow, and let them know that the dreamers can still shake hands
#             move_list.append(node)
#             for child_node in list(reversed(problem.getSuccessors(node[0]))):
#                 stack.push(child_node)
#                 
#                 
#         else:
#             move_list.remove(node)
#     print move_list
#     
#     return [x[1] for x in move_list]



#     nodes.push(fringe.pop())
    #set up system
    
    #here's what to do:
    #push fringe items of node from node stack onto fringe stack
    #for each fringe item, if it has successors, push to node stack
    #
    
    
#     while not fringe.isEmpty():
#         curr_node = fringe.pop()
#         nodes.push(curr_node)
#         visited.append(curr_node[0])
#         if problem.isGoalState(curr_node[0]):
#             return [x[1] for x in nodes.list]
#         print "testing node at position: ",curr_node[0]
# #             prev_moves = [move_list.pop()]
# #             move_list.push(prev_moves)
# #             curr_moves = prev_moves.append(curr_node[1])
# #             move_list.push(curr_moves)
#         if problem.isGoalState(curr_node[0]):
#             return [x[1] for x in nodes.list]
#         
#         if problem.getSuccessors(curr_node[0]):
#             for child_node in list(reversed(problem.getSuccessors(curr_node[0]))):
#                 if child_node[0] not in visited:
#                     fringe.push(child_node)
#         else: 
#             nodes.pop()
#             

#         while not nodes.isEmpty():
#             while not fringe.isEmpty():
#                 curr_node = fringe.pop()
#                 
#                 #if current node's successors not in fringe or have been visited, pop node
#                 if curr_node[0] not in visited:
#                 
#                     visited.append(curr_node[0])
#                     
#                     if problem.getSuccessors(curr_node):
#                         nodes.push(curr_node)
#                     if problem.isGoalState(curr_node[0]):
#                         return nodes
#     nodes = util.Stack()
#     fringe = util.Stack()
#     visited = []
#     if problem.isGoalState(problem.getStartState()):
#         return []
#      
#     visited.append(problem.getStartState())
#  
#     for child_node in list(reversed(problem.getSuccessors(problem.getStartState()))): #list comp here to reverse the successors. order of successors goes NORTH > SOUTH > EAST > WEST
#         fringe.push(child_node)
#     curr_node = fringe.pop()
#     if not problem.isGoalState(curr_node):
#         while


#goodest version
#     to_be_opened = util.Stack()
#     
#     visited = [problem.getStartState()]
#     for child_node in problem.getSuccessors(problem.getStartState()):
#         to_be_opened.push([child_node])
#         
#     
#     while not to_be_opened.isEmpty():
#         #pop from fringe
# #          for x in to_be_opened.list:
# #             print "item #",x
#         curr_node = list(to_be_opened.pop())
#         #add this node to visited checklist to prevent its future expansion
#         visited.append(curr_node[-1][0])
#         
#         #now check if we're in goal state
#         if problem.isGoalState(curr_node[-1][0]):
#             print "success"
#             return [x[1] for x in list(curr_node)]
#         #push node's successors to fringe b/c depth first
#         list_of_successors = list(problem.getSuccessors(curr_node[-1][0]))
#         if list_of_successors:
# #             print "successors of node: ",curr_node," are: ",list_of_successors
#             for child_node in list_of_successors:
#                 print "unvisited child node of: ",curr_node[-1],"is: ",child_node
#                 if child_node[0] not in visited:
# #                     
#                     temp = curr_node
#                     temp.append(child_node)
#                     to_be_opened.push(temp)



    stack = util.Stack()
    closed = [problem.getStartState()]
    
    
    beginning = problem.getSuccessors(problem.getStartState())
    for child in beginning:
        stack.push([child])
    
    while not stack.isEmpty():
#         print "in loop"
        curr = stack.pop()
        
        state = curr[-1]
        #why 
        closed.append(state[0])
        
        if problem.isGoalState(state[0]):
            return [x[1] for x in curr]
        
        fringe = list(problem.getSuccessors(state[0]))
        for child in fringe:
            if child[0] not in closed:
                temp = list(curr)
                temp.append(child)
                stack.push(temp)

    
    
    




        
        
        #need to know when we pop off the last successor of a node, to then pop off its predecessor
        #FRINGE ITEMS are a plan to go from node to fringed node. S-A, S-B. not just A, B

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    queue = util.Queue()
    closed = [problem.getStartState()]
    beginning = problem.getSuccessors(problem.getStartState())
    for child in beginning:
        queue.push([child])
        #if it goes on the fringe, it needs to be closed to the graph
        closed.append(child[0])
        
    while not queue.isEmpty():
#         print "in loop"
        curr = queue.pop()
        state = curr[-1]

        if problem.isGoalState(state[0]):
            return [x[1] for x in curr]
        
        fringe = list(problem.getSuccessors(state[0]))
#         print fringe
        for child in fringe:
            if child[0] not in closed:
                closed.append(child[0])
                temp = list(curr)
                temp.append(child)
                queue.push(temp)
 

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    queue = util.PriorityQueue()
    closed = []
    queue.push(([(problem.getStartState(),None,0)],0),0)
#     beginning = problem.getSuccessors(problem.getStartState())
#     for child in beginning:
#         queue.push(([child],child[2]),child[2])
#     for x in queue.heap:
#         print x
#     return
    while not queue.isEmpty():
#         print "in loop"
        curr = queue.pop()
        state = curr[0][-1]
        cumulative_val = curr[1]
        
        if problem.isGoalState(state[0]):
            final = [x[1] for x in curr[0]]
            return final[1:]
#         print "is ",state," in closed? ",(state[0] in closed)
        if state[0] not in closed:
            closed.append(state[0])
    
            
            fringe = list(problem.getSuccessors(state[0]))
            for child in fringe:
                if child[0] not in closed:
    #                 closed.append(child[0])
    #                 print "from node: ",state," we add child: ",child
                    child_val = child[2]
                    temp = list(curr[0])
                    temp.append(child)
                    queue.push((temp,cumulative_val+child_val),cumulative_val+child_val)
                

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    queue = util.PriorityQueue()
    closed = []
    start_state = (problem.getStartState(),None,0)
    queue.push(([start_state],0),heuristic(start_state[0],problem))

    while not queue.isEmpty():
#         print "in loop"
        curr = queue.pop()
        state = curr[0][-1]
        cumulative_val = curr[1]
        
        if problem.isGoalState(state[0]):
            final = [x[1] for x in curr[0]]
            return final[1:]
#         print "is ",state," in closed? ",(state[0] in closed)
        if state[0] not in closed:
            closed.append(state[0])
    
            
            fringe = list(problem.getSuccessors(state[0]))
            for child in fringe:
                if child[0] not in closed:
    #                 closed.append(child[0])
    #                 print "from node: ",state," we add child: ",child
                    child_val = child[2]
                    temp = list(curr[0])
                    temp.append(child)
                    queue.push((temp,cumulative_val+child_val),cumulative_val+child_val + heuristic(child[0],problem))

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
