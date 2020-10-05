# A4 - Party Invitation

def removeFriends(friends, rounds):
    '''
    removeFriends() removes every friend following
    the rounds list argument

    -- param
    friends : list
    rounds : list

    -- return
    list
    '''

    return []
# end of removeFriends

### Testing area DO NOT EDIT BELOW
k = int(input())
r = int(input())

rounds = []
for i in range(r):
    rounds.append(int(input()))

friends = list(range(1,k+1))

for item in removeFriends(friends, rounds):
    print(item)
