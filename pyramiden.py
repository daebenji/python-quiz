
def half_pyramid(rows):
    print('Half pyramid...\n')
    for i in range(rows):
        print('*' * (i+1))


def inverted_half_pyramid(rows):
    print('\nHalf pyramid inverted...\n')
    for i in range(rows):
        print(' '*(rows-i-1) + '*'*(rows+1-rows+i))

def full_pyramid(rows):
    print('\nFull pyramid...\n')
    for i in range(rows):
        print(' '*(rows-i-1) + '*'*(2*i+1))

def inverted_pyramid(rows):
    print('\nInverted pyramid...\n')
    for i in reversed(range(rows)):
        print(' '*(rows-i-1) + '*'*(2*i+1))

half_pyramid(9)
inverted_half_pyramid(15)
full_pyramid(5)
inverted_pyramid(5)
