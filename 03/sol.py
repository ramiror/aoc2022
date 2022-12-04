with open('input.txt', 'r') as f:
    coms = []
    for line in f.readlines():
        line=line.strip()
        size=len(line)
        # print(size, size//2)
        c1=line[0:size//2]
        c2=line[size//2:size]
        s1=set(c1)
        s2=set(c2)
        com=s1.intersection(s2)
        # print(line)
        # print(c1,c2)
        # print(f'comunes: {com}')
        elem=list(com)[0]
        if elem.islower():
            p = ord(elem)-ord('a')+1
        else:
            p = ord(elem)-ord('A')+27
        print(f'comunes: {com} prio: {p}')
        coms.append(p)

    print(sum(coms))


