def do_twice(f, val):
    f(val)
    f(val)

def print_twice(spam):
    print spam
    print spam

do_twice(print_twice, 'spam')

def do_four(g, string):
    do_twice(g, string)
    do_twice(g, string)

do_four(print_twice, 'spam')
