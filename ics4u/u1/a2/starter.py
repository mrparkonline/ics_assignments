# A2

def magic(array):
    ''' magic() returns True if the 4x4 array is magic

    -- param
    array : list

    -- return
    boolean
    '''

    # your code starts here

    return False # this line is editable
# end of magic

# DO NOT EDIT ANYTHING BELOW
square = []
for c in range(4):
    square.append(input())

if magic(square):
    print('magic')
else:
    print('not magic')
