
from stripsProblem import on

# subgoals for problem1

problem4_subgoals = [
    {
#   order:
#          e
#          d
#          c
#          b
#          a
        on('b'): 'a',
        on('c'): 'b',
        on('d'): 'c',
        on('e'): 'd',
    },
    {
#   order:
#          a
#          b
#          c
#          d
#          e
        on('d'): 'e',
        on('c'): 'd',
        on('b'): 'c',
        on('a'): 'b',
    },
]
