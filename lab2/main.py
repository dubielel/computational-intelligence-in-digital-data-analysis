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
SubgoalSearcher(SubgoalForwardSTRIPS(blocks3)).subgoal_search()
# SubgoalSearcher(SubgoalForwardSTRIPS(blocks3, BlocksWorldHeuristic)).subgoal_search()