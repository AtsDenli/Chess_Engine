def toNotation(pos):
    move = ""
    match pos[1]:
        case 0:
            move += 'a'
        case 1:
            move += 'b'
        case 2:
            move += 'c'
        case 3:
            move += 'd'
        case 4:
            move += 'e'
        case 5:
            move += 'f'
        case 6:
            move += 'g'
        case 7:
            move += 'h'
    move += str(pos[0]+1)
    return move

def fromNotation(notation):
    pos = []
    match notation[0]:
        case 'a':
            pos.append('0')
        case 'b':
            pos.append('1')
        case 'c':
            pos.append('2')
        case 'd':
            pos.append('3')
        case 'e':
            pos.append('4')
        case 'f':
            pos.append('5')
        case 'g':
            pos.append('6')
        case 'h':
            pos.append('7')
    pos[1] = int(notation[0])-1
    return pos