from monkey import Monkey
from monkey import log

monkeys = []

monkeys.append(Monkey(
  starting_items=[63, 84, 80, 83, 84, 53, 88, 72],
  operation=lambda old: old * 11,
  test=lambda d: d % 13 == 0,
  if_true=4,
  if_false=7,
  monkeys=monkeys
))

monkeys.append(Monkey(
  starting_items=[67, 56, 92, 88, 84],
  operation=lambda old: old + 4,
  test=lambda d: d % 11 == 0,
  if_true=5,
  if_false=3,
  monkeys=monkeys
))

monkeys.append(Monkey(
  starting_items=[52],
  operation=lambda old: old * old,
  test=lambda d: d % 2 == 0,
  if_true=3,
  if_false=1,
  monkeys=monkeys
))

monkeys.append(Monkey(
  starting_items=[59, 53, 60, 92, 69, 72],
  operation=lambda old: old + 2,
  test=lambda d: d % 5 == 0,
  if_true=5,
  if_false=6,
  monkeys=monkeys
))

monkeys.append(Monkey(
  starting_items=[61, 52, 55, 61],
  operation=lambda old: old + 3,
  test=lambda d: d % 7 == 0,
  if_true=7,
  if_false=2,
  monkeys=monkeys
))

monkeys.append(Monkey(
  starting_items=[79, 53],
  operation=lambda old: old + 1,
  test=lambda d: d % 3 == 0,
  if_true=0,
  if_false=6,
  monkeys=monkeys
))

monkeys.append(Monkey(
  starting_items=[59, 86, 67, 95, 92, 77, 91],
  operation=lambda old: old + 5,
  test=lambda d: d % 19 == 0,
  if_true=4,
  if_false=0,
  monkeys=monkeys
))

monkeys.append(Monkey(
  starting_items=[58, 83, 89],
  operation=lambda old: old * 19,
  test=lambda d: d % 17 == 0,
  if_true=2,
  if_false=1,
  monkeys=monkeys
))

# checkpoints = [1, 20] + [1000 * n for n in range(1,11)]
for round in range(10000):
    # if round in checkpoints:
    #     prinsp(round)
    for index, monkey in enumerate(monkeys):
        log(f'Monkey {index}:')
        monkey.play()

inspections = sorted([m.inspected_item_count for m in monkeys], reverse=True)
print(inspections)
print(inspections[0] * inspections[1])
