from stripsProblem import on

# subgoals for problem2

problem5_subgoals = [
    {
#   order:
#          f
#          g  d
#          h  e
        on('g'): 'h',
        on('f'): 'g',

        on('d'): 'e',
    },
    {
#   order:
#          a
#          b  e
#          c  d
        on('b'): 'c',
        on('a'): 'b',

        on('e'): 'd',
    },
]
