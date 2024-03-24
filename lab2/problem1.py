from stripsProblem import on, clear


problem1_blocks = { 'a', 'b', 'c', 'd', 'e' }

problem1_initial_state = {
#        d
#        b
#        c
#        a   e
#     -----------
#        table
    on('a'): 'table', clear('a'): False,
    on('c'): 'a', clear('c'): False,
    on('b'): 'c', clear('b'): False,
    on('d'): 'b', clear('d'): True,

    on('e'): 'table', clear('e'): True,
}

problem1_goal = {
#       a  b
#       e  c  d
#     -----------
#        table
    on('e'): 'table',
    on('a'): 'e',

    on('c'): 'table',
    on('b'): 'c',

    on('d'): 'table',
}
