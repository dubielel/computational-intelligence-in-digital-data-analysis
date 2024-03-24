from stripsProblem import on, clear

problem7_blocks = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' }

problem7_initial_state = {
#             f
#             c
#       g  e  b
#       a  d  h
#     -----------
#        table
    on('a'): 'table', clear('a'): False,
    on('g'): 'a', clear('g'): True,

    on('d'): 'table', clear('d'): False,
    on('e'): 'd', clear('e'): True,

    on('h'): 'table', clear('h'): False,
    on('b'): 'h',  clear('b'): False,
    on('c'): 'b', clear('c'): False,
    on('f'): 'c', clear('f'): True,
}

problem7_goal = {
#   order:
#            a
#         d  b  c
#         e  f  g
#   h can be wherever
    on('d'): 'e',
    on('b') : 'f',
    on('a'): 'b',
    on('c'): 'g'
}

problem7_subgoals = [
    {
#   order:
#          d
#          a
#          h
#          b
        on('d'): 'a',
        on('a'): 'h',
        on('h'): 'b',
    },
    {
#   order:
#          g
#          d
#          c
#          h
        on('g'): 'd',
        on('d'): 'c',
        on('c'): 'h',
    },
    {
#   order:
#          a
#          c
        on('a'): 'c'
    },
]