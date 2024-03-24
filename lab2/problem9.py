from stripsProblem import on, clear

problem9_blocks = { 'a', 'b', 'c', 'd', 'e', 'f' }

problem9_initial_state = {
#        e   f
#        d   c
#        a   b
#     -----------
#        table
    on('a'): 'table', clear('a'): False,
    on('d'): 'a', clear('d'): False,
    on('e'): 'd', clear('e'): True,

    on('b'): 'table', clear('b'): False,
    on('c'): 'b', clear('c'): False,
    on('f'): 'c', clear('f'): True,
}

problem9_goal = {
#   order:
#          e  a
#          b  c
#   d, f can be wherever
    on('b'): 'e',
    on('a'): 'c',
}

problem9_subgoals = [
    {
#   order:
#          d
#          b
#          c
#          d
#          e
#          f
        on('a'): 'b',
        on('b'): 'c',
        on('c'): 'd',
        on('d'): 'e',
        on('e'): 'f',
    },
    {
#   order:
#          a    f
#          e    b
#          d
#        table
        on('d'): 'table',
        on('e'): 'd',
        on('a'): 'e',
        on('f'): 'b',
    },
    {
#   order:
#          a
#          f
#          c  e
#          d  b
        on('a'): 'f',
        on('f'): 'c',
        on('c'): 'd',
        on('e'): 'b',
    },
]
