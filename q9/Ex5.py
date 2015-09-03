def gridline():
    print '+ ----',

def side():
    print '|     ',

def do_twice(f):
    f()
    f()

def make_top():
    do_twice(gridline)
    print '+'

def do_four(g):
    do_twice(g)
    do_twice(g)

def make_space():
    do_twice(side)
    print '|'

def make_grid():
    make_top()
    do_four(make_space)

do_twice(make_grid)
make_top()


################
################

def make_top2():
    do_four(gridline)
    print '+'

def make_space2():
    do_four(side)
    print '|'

def make_grid2():
    make_top2()
    do_four(make_space2)

do_four(make_grid2)
make_top2()
