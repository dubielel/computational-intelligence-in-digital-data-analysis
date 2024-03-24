from searchGeneric import AStarSearcher
from searchProblem import Path


class SubgoalSearcher(AStarSearcher):
    def subgoal_search(self):
        """returns (next) path from the problem's start node
        to a goal node. 
        Returns None if no path exists.
        """
        while not self.empty_frontier():
            self.path = self.frontier.pop()
            self.num_expanded += 1
            if self.problem.is_goal(self.path.end()):    # solution found
                self.solution = self.path   # store the solution found
                print(1, f"Solution for subproblem {self.problem.current_goal + 1}/{len(self.problem.goals)}: ",
                      str(self.path), f" (cost: {self.path.cost})\n",
                    self.num_expanded, "paths have been expanded and",
                            len(self.frontier), "paths remain in the frontier")
                self.frontier.clear()
                if not self.problem.new_goal(self.path.end()):
                    return self.path
            
            #print(4, f"Expanding: {self.path} (cost: {self.path.cost})")
            neighs = self.problem.neighbors(self.path.end())
            #print(2, f"Expanding: {self.path} with neighbors {neighs}")
            for arc in reversed(list(neighs)):
                self.add_to_frontier(Path(self.path,arc))
            # print(3, f"New frontier: {[p.end() for p in self.frontier]}")

        print(0,"No (more) solutions. Total of",
                     self.num_expanded,"paths expanded.")