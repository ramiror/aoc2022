def laburanding(team_items):
    print('laburanding')
    #first_team=False
    badge = \
        team_items[0].intersection(\
        team_items[1].intersection(\
        team_items[2]))
    print(badge)
    assert len(badge) == 1
    badge=list(badge)[0]
    if badge.islower():
        p = ord(badge)-ord('a')+1
    else:
        p = ord(badge)-ord('A')+27
    coms.append(p)

with open('input.txt', 'r') as f:
    first_team=True
    coms = []
    team_items = []
    for line in f.readlines():
        if len(team_items) % 3 == 0:
            if not first_team:
                laburanding(team_items)
                team_items = []
        print('normalito')
        team_items.append(set(line.strip()))
        first_team=False
    laburanding(team_items)
    team_items = []
    print(sum(coms))
