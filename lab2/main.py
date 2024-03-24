from SubgoalForwardStrips import SubgoalForwardSTRIPS
from SubgoalPlanningProblem import SubgoalPlanningProblem
from SubgoalSearcher import SubgoalSearcher
from heuristic import BlocksWorldHeuristic
from stripsProblem import *
from searchMPP import *
from stripsForwardPlanner import *
from searchGeneric import Searcher

blocks1_blocks = { 'a', 'b', 'c' }
blocks1_initial_state = {
#             b
#       a     c
#     -----------
#        table
    on('a'): 'table',
    clear('a'): True,
    on('b'): 'c',
    clear('b'): True,
    on('c'): 'table',
    clear('c'): False
}
blocks1_goal = {
#          c
#          a
#          b
#     -----------
#        table
    on('a'): 'b',
    on('c'): 'a'
}

blocks1_domain = create_blocks_world(blocks1_blocks)
blocks1 = Planning_problem(blocks1_domain, blocks1_initial_state, blocks1_goal)
print("=============================================================================================================================================================================================================================================================================================")
# AStarSearcher(Forward_STRIPS(blocks1)).search()

# ZADANIE 1
blocks2_blocks = { 'a', 'b', 'c', 'd', 'e' }
blocks2_initial_state = {
#          b  e
#       a  c  d
#     -----------
#        table
    on('a'): 'table',
    clear('a'): True,
    on('b'): 'c',
    clear('b'): True,
    on('c'): 'table',
    clear('c'): False,
    on('d'): 'table',
    clear('d'): False,
    on('e'): 'd',
    clear('e'): True
}
blocks2_goal = {
#          c
#          a
#          b
#          d
#          e
#     -----------
#        table
    on('d'): 'e',
    on('b'): 'd',
    on('a'): 'b',
    on('c'): 'a'
}

blocks2_domain = create_blocks_world(blocks2_blocks)
blocks2 = Planning_problem(blocks2_domain, blocks2_initial_state, blocks2_goal)
print("=============================================================================================================================================================================================================================================================================================")
blocks2_heuristic = BlocksWorldHeuristic(blocks2)
# AStarSearcher(Forward_STRIPS(blocks2)).search()
# AStarSearcher(Forward_STRIPS(blocks2, blocks2_heuristic)).search()


blocks3_blocks = { 'a', 'b', 'c', 'd', 'e' }
blocks3_initial_state = {
#          b  e
#       a  c  d
#     -----------
#        table
    on('a'): 'table',
    clear('a'): True,
    on('b'): 'c',
    clear('b'): True,
    on('c'): 'table',
    clear('c'): False,
    on('d'): 'table',
    clear('d'): False,
    on('e'): 'd',
    clear('e'): True
}
blocks3_goals = [
    { on('d'): 'a' },
    { on('d'): 'c' },
    {
#              c
#              a
#              b
#              d
#              e
#         -----------
#            table
        on('d'): 'e',
        on('b'): 'd',
        on('a'): 'b',
        on('c'): 'a'
    }
]

blocks3_domain = create_blocks_world(blocks3_blocks)
blocks3 = SubgoalPlanningProblem(blocks3_domain, blocks3_initial_state, blocks3_goals)
# SubgoalSearcher(SubgoalForwardSTRIPS(blocks3)).subgoal_search()
# SubgoalSearcher(SubgoalForwardSTRIPS(blocks3, BlocksWorldHeuristic)).subgoal_search()


# ZADANIE3
blocks4dom = create_blocks_world({'a','b','c', 'd', 'e', 'f', 'g', 'h'})
blocks4 = SubgoalPlanningProblem(blocks4dom,
     {
          on('a'):'table', clear('a'): False,
          on('b'):'h',  clear('b'): False,
          on('c'):'b', clear('c'): False,
          on('d'):'table', clear('d'): False,
          on('e'): 'd', clear('e'): True,
          on('f'): 'c', clear('f'): True,
          on('g'): 'a', clear('g'): True,
          on('h'):'table', clear('h'): False,
     }, # initial state
     [
          {on('d'): 'a', on('a'): 'h', on('h'): 'b'}, 
          {on('d'): 'c', on('c'): 'h', on('g'): 'd'},
          {on('a'): 'c'},
          {on('d'): 'e', on('b') : 'f', on('a'):'b', on('c'):'g'}
     ])  #goal
# SubgoalSearcher(SubgoalForwardSTRIPS(blocks4)).subgoal_search()
# SubgoalSearcher(SubgoalForwardSTRIPS(blocks4, BlocksWorldHeuristic)).subgoal_search()


blocks5dom = create_blocks_world({'a','b','c', 'd', 'e', 'f', 'g'})
blocks5 = SubgoalPlanningProblem(blocks5dom,
     {
          on('a'):'table', clear('a'): False,
          on('b'):'table',  clear('b'): False,
          on('c'):'b', clear('c'): False,
          on('d'):'table', clear('d'): False,
          on('e'): 'd', clear('e'): True,
          on('f'): 'c', clear('f'): True,
          on('g'): 'a', clear('g'): True,
     }, # initial state
     [
          {on('a'): 'f'},
          {on('d'): 'e', on('b') : 'f', on('a'):'b', on('c'):'g'},
          {on('d'): 'a', on('a'): 'f', on('f'): 'b'}, 
          {on('d'): 'c', on('c'): 'f', on('g'): 'd'},
          {on('a'): 'c'},
          
     ])  #goal
# SubgoalSearcher(SubgoalForwardSTRIPS(blocks5)).subgoal_search()
# SubgoalSearcher(SubgoalForwardSTRIPS(blocks5, BlocksWorldHeuristic)).subgoal_search()


blocks6dom = create_blocks_world({'a','b','c', 'd', 'e', 'f'})
blocks6 = SubgoalPlanningProblem(blocks6dom,
     {
          on('a'):'table', clear('a'): False,
          on('b'):'table',  clear('b'): False,
          on('c'):'b', clear('c'): False,
          on('d'):'a', clear('d'): False,
          on('e'): 'd', clear('e'): True,
          on('f'): 'c', clear('f'): True,
     }, # initial state
     [
          {on('a'): 'b', on('b'): 'c', on('c'): 'd', on('d'): 'e', on('e'): 'f'},
          {on('d'): 'table', on('e'): 'd', on('a'): 'e', on('f'): 'b'},
          {on('a'): 'f', on('f'): 'c', on('c'): 'd', on('e'): 'b'},
          {on('b'): 'e', on('a'): 'c'}  
     ])  #goal
# SubgoalSearcher(SubgoalForwardSTRIPS(blocks6)).subgoal_search()
SubgoalSearcher(SubgoalForwardSTRIPS(blocks6, BlocksWorldHeuristic)).subgoal_search()
