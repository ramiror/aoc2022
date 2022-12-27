with open('dibujin.tmp', 'r') as f:
    dibu=f.read().rstrip()

inp=[[c for c in line]
        for line in dibu.split('\n')]
#inp=inp[:-1]
import pprint
# pprint.pprint(inp)

lines=len(inp)
cols=len(inp[lines-1])
tra=[[inp[j][i] for j in range(lines)] for i in range(cols)]
# pprint.pprint(tra)

# reverse lines so bottom boxes are on the left
# to use lists' append and pop methods
for line in tra:
    line.reverse()
# pprint.pprint(tra)

for line in tra:
    while line[len(line)-1] == ' ':
        line.pop()
# pprint.pprint(tra)

def do_move(src, dst):
    tra[dst-1].append(tra[src-1].pop())

with open('instructions.tmp', 'r') as f:
    for move in f.readlines():
        _, amount, _, src, _, dst = move.split()
        amount=int(amount)
        src=int(src)
        dst=int(dst)
        # print(amount, src, dst)
        for count in range(amount):
            do_move(src, dst)

print(''.join([line[-1] for line in tra]))
