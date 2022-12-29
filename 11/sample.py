class Monkey:
    def __init__(self,
            starting_items,
            operation,
            test,
            if_true,
            if_false,
            monkeys):
        self.starting_items = starting_items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.monkeys = monkeys
        self.inspected_item_count = 0

    def play(self):
        if len(self.starting_items) == 0:
            return
        while len(self.starting_items) > 0:
            worry_level = self.starting_items.pop(0)
            monkey, worry_level = self.test_item(worry_level)
            monkeys[monkey].starting_items.append(worry_level)

    def test_item(self, worry_level):
        worry_level = self.operation(worry_level)
        worry_level %= (19*23*13*17)
        self.inspected_item_count+=1
        return self.if_true if self.test(worry_level) else self.if_false, worry_level

monkeys = []

monkeys.append(Monkey(
  starting_items=[79, 98],
  operation=lambda old: old * 19,
  test=lambda d: d % 23 == 0,
  if_true=2,
  if_false=3,
  monkeys=monkeys
))

monkeys.append(Monkey(
  starting_items=[54, 65, 75, 74],
  operation=lambda old: old + 6,
  test=lambda d: d % 19 == 0,
  if_true=2,
  if_false=0,
  monkeys=monkeys
))

monkeys.append(Monkey(
  starting_items=[79, 60, 97],
  operation=lambda old: old * old,
  test=lambda d: d % 13 == 0,
  if_true=1,
  if_false=3,
  monkeys=monkeys
))

monkeys.append(Monkey(
  starting_items=[74],
  operation=lambda old: old + 3,
  test=lambda d: d % 17 == 0,
  if_true=0,
  if_false=1,
  monkeys=monkeys
))

# monkeys.append(Monkey(
#   starting_items=[63, 84, 80, 83, 84, 53, 88, 72],
#   operation=lambda old: old * 11,
#   test=lambda d: d % 13 == 0,
#   if_true=4,
#   if_false=7,
#   monkeys=monkeys
# ))
# 
# monkeys.append(Monkey(
#   starting_items=[67, 56, 92, 88, 84],
#   operation=lambda old: old + 4,
#   test=lambda d: d % 11 == 0,
#   if_true=5,
#   if_false=3,
#   monkeys=monkeys
# ))
# 
# monkeys.append(Monkey(
#   starting_items=[52],
#   operation=lambda old: old * old,
#   test=lambda d: d % 2 == 0,
#   if_true=3,
#   if_false=1,
#   monkeys=monkeys
# ))
# 
# monkeys.append(Monkey(
#   starting_items=[59, 53, 60, 92, 69, 72],
#   operation=lambda old: old + 2,
#   test=lambda d: d % 5 == 0,
#   if_true=5,
#   if_false=6,
#   monkeys=monkeys
# ))
# 
# monkeys.append(Monkey(
#   starting_items=[61, 52, 55, 61],
#   operation=lambda old: old + 3,
#   test=lambda d: d % 7 == 0,
#   if_true=7,
#   if_false=2,
#   monkeys=monkeys
# ))
# 
# monkeys.append(Monkey(
#   starting_items=[79, 53],
#   operation=lambda old: old + 1,
#   test=lambda d: d % 3 == 0,
#   if_true=0,
#   if_false=6,
#   monkeys=monkeys
# ))
# 
# monkeys.append(Monkey(
#   starting_items=[59, 86, 67, 95, 92, 77, 91],
#   operation=lambda old: old + 5,
#   test=lambda d: d % 19 == 0,
#   if_true=4,
#   if_false=0,
#   monkeys=monkeys
# ))
# 
# monkeys.append(Monkey(
#   starting_items=[58, 83, 89],
#   operation=lambda old: old * 19,
#   test=lambda d: d % 17 == 0,
#   if_true=2,
#   if_false=1,
#   monkeys=monkeys
# ))

def prinsp(round):
    print(f'{round} rounds:')
    inspection_counts = [monkey.inspected_item_count for monkey in monkeys]
    print(inspection_counts)
    inspection_counts.sort(reverse=True)
    print(inspection_counts[0] * inspection_counts[1])

checkpoints = [1, 20] + [1000 * n for n in range(1,11)]
for round in range(10000):
    if round in checkpoints:
        prinsp(round)
    for monkey in monkeys:
        monkey.play()
