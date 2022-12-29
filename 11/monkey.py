def log(msg):
    pass

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
        # log(f'  Starring items: {self.starting_items}')
        # log(f'  Operation: {self.operation}')
        # log(f'  Test: {self.test}')
        # log(f'    If true: {self.if_true}')
        # log(f'    If false: {self.if_false}')
        if len(self.starting_items) == 0:
            return
        while len(self.starting_items) > 0:
            worry_level = self.starting_items.pop(0)
            log(f'  Monkey inspects an item with a worry level of {worry_level}.')
            monkey, worry_level = self.test_item(worry_level)
            log(f'    Worry level is operated to: {worry_level}')
            self.monkeys[monkey].starting_items.append(worry_level)

    def test_item(self, worry_level):
        worry_level = self.operation(worry_level)
        worry_level %= (2*3*5*7*11*13*17*19)
        self.inspected_item_count+=1
        return self.if_true if self.test(worry_level) else self.if_false, worry_level

