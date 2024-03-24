from stripsProblem import on, clear

problem8_blocks = { 'a', 'b', 'c', 'd', 'e', 'f', 'g' }

problem8_initial_state = {
#          f
#       g  c  e
#       a  b  d
#     -----------
#        table
    on('a'): 'table', clear('a'): False,
    on('g'): 'a', clear('g'): True,

    on('b'): 'table', clear('b'): False,
    on('c'): 'b', clear('c'): False,
    on('f'): 'c', clear('f'): True,

    on('d'): 'table', clear('d'): False,
    on('e'): 'd', clear('e'): True,
}

problem8_goal = {
#   order:
#          a
#          c
#   b, d, e, f, g can be wherever
    on('a'): 'c'
}

problem8_subgoals = [
    {
#   order:
#          a
#          f
        on('a'): 'f',
    },
    {
#   order:
#             a
#          e  b  c
#          d  f  g
        on('d'): 'e',
        on('b'): 'f',
        on('a'): 'b',
        on('c'): 'g',
    },
    {
#   order:
#          d
#          a
#          f
#          b
        on('d'): 'a',
        on('a'): 'f',
        on('f'): 'b',
    }, 
    {
#   order:
#          g
#          d
#          c
#          f
        on('g'): 'd',
        on('d'): 'c',
        on('c'): 'f',
    },
]
