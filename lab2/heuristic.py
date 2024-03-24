from copy import deepcopy
from typing import Dict, List
from stripsProblem import Planning_problem

class BlocksWorldHeuristic():

    def __init__(self, problem: Planning_problem) -> None:
        self.expected_columns = self._calculate_columns(problem.goal)
        self.expected_fundaments = self._calculate_fundaments(problem.goal)
        
    def _get_unique_blocks(self, goal):
        unique_blocks = set()
        for k, v in goal.items():
            if v != 'table':
                unique_blocks.add(v) 
            if k[0] != 'table':
                unique_blocks.add(k[0])
        
        return unique_blocks

    def _calculate_columns(self, goal) -> Dict[str, int]:
        processed_goal = {k[0]: v for k, v in goal.items()}
        result = {}
        for block in self._get_unique_blocks(goal):
            curr = block
            depth = 0

            while curr in processed_goal and processed_goal[curr] != 'table':
                curr = processed_goal[curr]
                depth += 1

            result[block] = depth

        return result


    def _calculate_fundaments(self, goal) -> Dict[str, List[str]]:
        processed_goal = {k[0]: v for k, v in goal.items()}
        result = {}
        for block in self._get_unique_blocks(goal):
            curr = block
            fundament = []

            while curr in processed_goal and processed_goal[curr] != 'table':
                curr = processed_goal[curr]
                fundament.append(curr)

            result[block] = fundament

        return result

    def __call__(self, state, *args) -> int:
        
        temp = {k : v for k, v in state.items() if not k.startswith('clear') }
        state_columns = self._calculate_columns(temp)
        state_fundaments = self._calculate_fundaments(temp)

        result = 0
        checked = []

        for element, expected_column in self.expected_columns.items():
            if expected_column != state_columns[element]:
                result += 1
                checked.append(element)

        for element, expected_fundaments in self.expected_fundaments.items():
            if element in checked:
                continue

            for i, value in enumerate(expected_fundaments):
                if value != state_fundaments[element][i]:
                    result += 2

        return result