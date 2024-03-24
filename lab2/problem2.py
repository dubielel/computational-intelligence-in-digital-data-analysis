from stripsProblem import on, clear


problem2_blocks = { 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h' }

problem2_initial_state = {
#       f     d
#       g  b  c
#       a  h  e
#     -----------
#        table
    on('a'): 'table', clear('a'): False,
    on('g'): 'a', clear('g'): False,
    on('f'): 'g', clear('f'): True,

    on('h'): 'table', clear('h'): False,
    on('b'): 'h', clear('b'): True,

    on('e'): 'table', clear('e'): False,
    on('c'): 'e', clear('c'): False,
    on('d'): 'c', clear('d'): True,
}

problem2_goal = {
#       d     g
#       b     e
#       a     h
#       f     c
#     -----------
#        table
    on('f'): 'table',
    on('a'): 'f',
    on('b'): 'a',
    on('d'): 'b',

    on('c'): 'table',
    on('h'): 'c',
    on('e'): 'h',
    on('g'): 'e',
}
