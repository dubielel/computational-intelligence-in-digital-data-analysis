from stripsProblem import on, clear

problem3_blocks = { 'a', 'b', 'c', 'd', 'e' }

problem3_initial_state = {
#          b  e
#       a  c  d
#     -----------
#        table
    on('a'): 'table', clear('a'): True,

    on('c'): 'table', clear('c'): False,
    on('b'): 'c', clear('b'): True,

    on('d'): 'table', clear('d'): False,
    on('e'): 'd', clear('e'): True
}

problem3_goal = {
#   order:
#          c
#          a
#          b
#          d
#          e
    on('d'): 'e',
    on('b'): 'd',
    on('a'): 'b',
    on('c'): 'a'
}