chars = [char for char in input()]
from collections import Counter
limit = len(chars)
pointer = 0
while True:
  if pointer >= limit:
    print('No marker')
    exit(-1)
  repes = dict(Counter(chars[pointer:pointer+14]))
  if (all(count == 1 for count in repes.values())):
    print(pointer + 14)
    exit()
  pointer += 1
