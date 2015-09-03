def right_justify(s):
    line = ''
    for i in range(0, 70):
        if i < 70-len(s):
            line = line + ' '
        else:
            line = line + str(s[i-(70-len(s))])
    print line

right_justify('The mountain came over the edge of the horizon')
