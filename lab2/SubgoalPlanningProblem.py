class SubgoalPlanningProblem(object):
    def __init__(self, prob_domain, initial_state, goals):
        """
        a planning problem consists of
        * a planning domain
        * the initial state
        * a goal 
        """
        self.prob_domain = prob_domain
        self.initial_state = initial_state
        self.goals = goals