from copy import deepcopy
from typing import Dict, List
from stripsProblem import Planning_problem

class BlocksWorldNaiveHeuristic():

    def __init__(self, problem: Planning_problem) -> None:
        self.expected_columns = self._calculate_columns(problem.goal)
        self.expected_fundaments = self._calculate_fundaments(problem.goal)


    def _calculate_columns(self, goal) -> Dict[str, int]:
        unique_blocks = set()
        for k, v in goal.items():
            if v != 'table':
                unique_blocks.add(v) 
            if k[0] != 'table':
                unique_blocks.add(k[0])
       

        goal = {k[0]: v for k, v in goal.items()}

        result = dict()
        for block in unique_blocks:
            curr = block
            deepness = 0

            while curr in goal and goal[curr] != 'table':
                curr = goal[curr]
                deepness += 1

            result[block] = deepness

        return result
        # TODO:
        # return a dict of form:
        # { <block name> : <index of column in the goal state> }


    def _calculate_fundaments(self, goal) -> Dict[str, List[str]]:
        # TODO:
        # return a dict of form:
        # { <block name> : <list of the blocks below it in the goal state> }
        unique_blocks = set()
        for k, v in goal.items():
            if v != 'table':
                unique_blocks.add(v) 
            if k[0] != 'table':
                unique_blocks.add(k[0])   

        goal = {k[0]: v for k, v in goal.items()}

        result = dict()
        for block in unique_blocks:
            curr = block
            temp = list()

            while curr in goal and goal[curr] != 'table':
                curr = goal[curr]
                temp.append(curr)

            result[block] = temp

        return result

    def __call__(self, state, *args) -> int:
        
        temp = {k : v for k, v in state.items() if not k.startswith('clear') }
        state_columns = self._calculate_columns(temp)
        state_fundaments = self._calculate_fundaments(temp)

        result = 0
        checked = list()

        for element, expectedColumn in self.expected_columns.items():
            if element not in state_columns:
                print(state)
                print(state_columns)


            if expectedColumn != state_columns[element]:
                result += 1
                checked.append(element)

        for element, expectedFundaments in self.expected_fundaments.items():
            if element in checked:
                continue

            for i in range(len(expectedFundaments)):
                if expectedFundaments[i] != state_fundaments[element][i]:
                    result += 2

        return result
        # TODO:
        # - add 1 to the heuristic value per each block placed in an incorrect column
        # - for other blocks, add 2 if their fundament is incorrect 
        # tip. use self.expected_columns and self.expected_fundaments