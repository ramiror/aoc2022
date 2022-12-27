import sys

root = {}
for line in sys.stdin:
    line = line.rstrip()
    # print(line)
    # print('/: ', root)

    if line.startswith('$'):
        is_data = False
    if '$ ls' == line:
        is_data = True
        continue

    if is_data:
        size_or_dir, name = line.split()
        if 'dir' == size_or_dir:
            pointer[name]={'..': pointer, '__size__': 0} # trucazo
            continue
        else:
            size = int(size_or_dir)
            pointer['__size__']=pointer.get('__size__', 0) + size

    if '$ cd /' == line:
        pointer = root
    elif '$ cd ..' == line:
        pointer = pointer.get('..')
    elif line.startswith('$ cd'):
        _, _, dirname = line.split()
        pointer = pointer.get(dirname)

# find dirs smaller than 100001

def node_size(node, path):
    size=0
    for key, value in node.items():
        if '..' == key:
            continue
        if '__size__' == key:
            size += value
        else:
            size += sum(size[1] for size in node_size(value, [key] + path))
    if size <= 100000:
        print(size)
    yield path, size

for dir_size in node_size(root, ['/']):
    pass # print(dir_size)
