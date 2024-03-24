from SubgoalForwardStrips import SubgoalForwardSTRIPS
from SubgoalPlanningProblem import SubgoalPlanningProblem
from SubgoalSearcher import SubgoalSearcher
from heuristic import BlocksWorldHeuristic
from stripsProblem import *
from searchMPP import *
from stripsForwardPlanner import *
from searchGeneric import Searcher


blocks1dom = create_blocks_world({'a','b','c'})
blocks1 = Planning_problem(blocks1dom,
     {on('a'):'table', clear('a'):True,
      on('b'):'c',  clear('b'):True,
      on('c'):'table', clear('c'):False}, # initial state
     {on('a'):'b', on('c'):'a'})  #goal
print("=============================================================================================================================================================================================================================================================================================")
# AStarSearcher(Forward_STRIPS(blocks1)).search()

# ZADANIE 1
blocks2dom = create_blocks_world({'a','b','c', 'd', 'e'})
blocks2 = Planning_problem(blocks2dom,
     {on('a'):'table', clear('a'):True,
      on('b'):'c',  clear('b'):True,
      on('c'):'table', clear('c'):False,
      on('d'):'table', clear('d'): False,
      on('e'): 'd', clear('e'): True}, # initial state
     {on('d'): 'e', on('b') : 'd', on('a'):'b', on('c'):'a'})  #goal
print("=============================================================================================================================================================================================================================================================================================")
heur2 = BlocksWorldHeuristic(blocks2)
# AStarSearcher(Forward_STRIPS(blocks2)).search()
# AStarSearcher(Forward_STRIPS(blocks2, heur2)).search()


# ZADANIE 2
blocks3dom = create_blocks_world({'a','b','c', 'd', 'e'})
blocks3 = SubgoalPlanningProblem(blocks3dom,
     {
          on('a'):'table', clear('a'):True,
          on('b'):'c',  clear('b'):True,
          on('c'):'table', clear('c'):False,
          on('d'):'table', clear('d'): False,
          on('e'): 'd', clear('e'): True
     }, # initial state
     [
          {on('d'): 'a'}, 
          {on('d'): 'c'}, 
          {on('d'): 'e', on('b') : 'd', on('a'):'b', on('c'):'a'}
     ])  #goal
SubgoalSearcher(SubgoalForwardSTRIPS(blocks3)).subgoal_search()
# SubgoalSearcher(SubgoalForwardSTRIPS(blocks3, BlocksWorldHeuristic)).subgoal_search()
