from stripsForwardPlanner import State
from SubgoalPlanningProblem import SubgoalPlanningProblem
from searchProblem import Arc, Search_problem
from stripsForwardPlanner import Forward_STRIPS, zero
from stripsProblem import Planning_problem


class SubgoalForwardSTRIPS(Search_problem):
    def __init__(self, planning_problem: SubgoalPlanningProblem, heur_class=None):
        """creates a forward search space from a planning problem.
        heur(state,goal) is a heuristic function,
           an underestimate of the cost from state to goal, where
           both state and goals are feature:value dictionaries.
        """
        self.prob_domain = planning_problem.prob_domain
        self.initial_state = State(planning_problem.initial_state)
        self.goals = planning_problem.goals
        self.current_goal = 0
        self.heur_class = heur_class
        self.heur = self._make_heur(heur_class, self.initial_state)

    def is_goal(self, state):
        """is True if node is a goal.

        Every goal feature has the same value in the state and the goal."""
        return all(state.assignment[prop]==self.goals[self.current_goal][prop]
                   for prop in self.goals[self.current_goal])
        
    def new_goal(self):
        self.current_goal += 1
        if self.current_goal == len(self.goals):
            return None
        return self.goals[self.current_goal]
         

    def start_node(self):
        """returns start node"""
        return self.initial_state

    def neighbors(self,state):
        """returns neighbors of state in this problem"""
        return [ Arc(state, self.effect(act,state.assignment), act.cost, act)
                 for act in self.prob_domain.actions
                 if self.possible(act,state.assignment)]

    def possible(self,act,state_asst):
        """True if act is possible in state.
        act is possible if all of its preconditions have the same value in the state"""
        return all(state_asst[pre] == act.preconds[pre]
                   for pre in act.preconds)

    def effect(self,act,state_asst):
        """returns the state that is the effect of doing act given state_asst
        Python 3.9:  return state_asst | act.effects"""
        new_state_asst = state_asst.copy()
        new_state_asst.update(act.effects)
        return State(new_state_asst)
    
    def heuristic(self,state):
        """in the forward planner a node is a state.
        the heuristic is an (under)estimate of the cost
        of going from the state to the top-level goal.
        """
        return self.heur[self.current_goal](state.assignment, self.goals[self.current_goal])
    
    def new_heur(self):
        if not heur_class:
            return [zero for _ in self.goals]
        heurs = []
        
        for goal in self.goals:
            planning_problem = Planning_problem(self.prob_domain, self.initial_state)