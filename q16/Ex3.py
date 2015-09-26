def checkfermat(a,b,c,n):
    thesum = a ** n + b ** n
    check = c ** n

    if n > 2 and thesum == check:
        print "Holy Smokes, Fermat was wrong!"
    else:
        print "No, that doesn't work."

def inputs():
    a = int(raw_input())
    b = int(raw_input())
    c = int(raw_input())
    n = int(raw_input())
    checkfermat(a,b,c,n)

inputs()
