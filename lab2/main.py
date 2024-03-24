from SubgoalForwardStrips import SubgoalForwardSTRIPS
from SubgoalPlanningProblem import SubgoalPlanningProblem
from SubgoalSearcher import SubgoalSearcher
from heuristic import BlocksWorldHeuristic
from stripsProblem import *
from searchMPP import *
from stripsForwardPlanner import *
from time import perf_counter

from problem1 import *
from problem2 import *
from problem3 import *

from problem4 import *
from problem5 import *
from problem6 import *

from problem7 import *
from problem8 import *
from problem9 import *


# 3.0
problem1_domain = create_blocks_world(problem1_blocks)
problem1 = Planning_problem(
    problem1_domain,
    problem1_initial_state,
    problem1_goal
)
problem1_heuristic = BlocksWorldHeuristic(problem1)

# start = perf_counter()
# AStarSearcher(Forward_STRIPS(problem1)).search()
# end = perf_counter()
# print(f'Time: {end - start}')

# start = perf_counter()
# AStarSearcher(Forward_STRIPS(problem1, problem1_heuristic)).search()
# end = perf_counter()
# print(f'Time: {end - start}')


problem2_domain = create_blocks_world(problem2_blocks)
problem2 = Planning_problem(
    problem2_domain,
    problem2_initial_state,
    problem2_goal
)
problem2_heuristic = BlocksWorldHeuristic(problem2)

# start = perf_counter()
# AStarSearcher(Forward_STRIPS(problem2)).search()
# end = perf_counter()
# print(f'Time: {end - start}')

# start = perf_counter()
# AStarSearcher(Forward_STRIPS(problem2, problem2_heuristic)).search()
# end = perf_counter()
# print(f'Time: {end - start}')


problem3_domain = create_blocks_world(problem3_blocks)
problem3 = Planning_problem(
    problem3_domain,
    problem3_initial_state,
    problem3_goal
)
problem3_heuristic = BlocksWorldHeuristic(problem3)

# start = perf_counter()
# AStarSearcher(Forward_STRIPS(problem3)).search()
# end = perf_counter()
# print(f'Time: {end - start}')

# start = perf_counter()
# AStarSearcher(Forward_STRIPS(problem3, problem3_heuristic)).search()
# end = perf_counter()
# print(f'Time: {end - start}')


# 4.0
# problem1 is expanded with subgoals
problem4_domain = create_blocks_world(problem1_blocks)
problem4 = SubgoalPlanningProblem(
    problem4_domain,
    problem1_initial_state,
    [*problem4_subgoals, problem1_goal]
)

# start = perf_counter()
# SubgoalSearcher(SubgoalForwardSTRIPS(problem4)).subgoal_search()
# end = perf_counter()
# print(f'Time: {end - start}')

# start = perf_counter()
# SubgoalSearcher(SubgoalForwardSTRIPS(problem4, BlocksWorldHeuristic)).subgoal_search()
# end = perf_counter()
# print(f'Time: {end - start}')


# problem2 is expanded with subgoals
problem5_domain = create_blocks_world(problem2_blocks)
problem5 = SubgoalPlanningProblem(
    problem5_domain,
    problem2_initial_state,
    [*problem5_subgoals, problem2_goal]
)

# start = perf_counter()
# SubgoalSearcher(SubgoalForwardSTRIPS(problem5)).subgoal_search()
# end = perf_counter()
# print(f'Time: {end - start}')

# start = perf_counter()
# SubgoalSearcher(SubgoalForwardSTRIPS(problem5, BlocksWorldHeuristic)).subgoal_search()
# end = perf_counter()
# print(f'Time: {end - start}')


# problem3 is expanded with subgoals
problem6_domain = create_blocks_world(problem3_blocks)
problem6 = SubgoalPlanningProblem(
    problem6_domain,
    problem3_initial_state,
    [*problem6_subgoals, problem3_goal]
)

# start = perf_counter()
# SubgoalSearcher(SubgoalForwardSTRIPS(problem6)).subgoal_search()
# end = perf_counter()
# print(f'Time: {end - start}')

# start = perf_counter()
# SubgoalSearcher(SubgoalForwardSTRIPS(problem6, BlocksWorldHeuristic)).subgoal_search()
# end = perf_counter()
# print(f'Time: {end - start}')


# 5.0
problem7_domain = create_blocks_world(problem7_blocks)
problem7 = SubgoalPlanningProblem(
    problem7_domain,
    problem7_initial_state,
    [*problem7_subgoals, problem7_goal]
)

# start = perf_counter()
# SubgoalSearcher(SubgoalForwardSTRIPS(problem7)).subgoal_search()
# end = perf_counter()
# print(f'Time: {end - start}')

# start = perf_counter()
# SubgoalSearcher(SubgoalForwardSTRIPS(problem7, BlocksWorldHeuristic)).subgoal_search()
# end = perf_counter()
# print(f'Time: {end - start}')


problem8_domain = create_blocks_world(problem8_blocks)
problem8 = SubgoalPlanningProblem(
    problem8_domain,
    problem8_initial_state,
    [*problem8_subgoals, problem8_goal]
)

# start = perf_counter()
# SubgoalSearcher(SubgoalForwardSTRIPS(problem8)).subgoal_search()
# end = perf_counter()
# print(f'Time: {end - start}')

# start = perf_counter()
# SubgoalSearcher(SubgoalForwardSTRIPS(problem8, BlocksWorldHeuristic)).subgoal_search()
# end = perf_counter()
# print(f'Time: {end - start}')


problem9_domain = create_blocks_world(problem9_blocks)
problem9 = SubgoalPlanningProblem(
    problem9_domain,
    problem9_initial_state,
    [*problem9_subgoals, problem9_goal]
)

# start = perf_counter()
# SubgoalSearcher(SubgoalForwardSTRIPS(problem9)).subgoal_search()
# end = perf_counter()
# print(f'Time: {end - start}')

# start = perf_counter()
# SubgoalSearcher(SubgoalForwardSTRIPS(problem9, BlocksWorldHeuristic)).subgoal_search()
# end = perf_counter()
# print(f'Time: {end - start}')
