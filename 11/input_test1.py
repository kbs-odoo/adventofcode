import sys

monkeys = {'mo_0': [89, 95, 92, 64, 87, 68], 'mo_1': [87, 67],'mo_2': [95, 79, 92, 82, 60], 'mo_3': [67, 97, 56],
           'mo_4': [80, 68, 87, 94, 61, 59, 50, 68], 'mo_5': [73, 51, 76, 59], 'mo_6': [92],
           'mo_7': [99, 76, 78, 76, 79, 90, 89]}
check_levels = {'mo_0': 0, 'mo_1': 0,'mo_2': 0, 'mo_3': 0, 'mo_4': 0, 'mo_5': 0, 'mo_6': 0, 'mo_7': 0}


def inspection(mo_list, true_monkey, false_monkey, operation, check_el, check_level_dict, operation_el=None):
    for old in monkeys[mo_list]:
        if operation_el:
            if operation == 'mul':
                new = old * operation_el
            elif operation == 'sub':
                new = old - operation_el
            elif operation == 'add':
                new = old + operation_el
            elif operation == 'div':
                new = old // operation_el
        else:
            if operation == 'mul':
                new = old * old
            elif operation == 'sub':
                new = old - old
            elif operation == 'add':
                new = old + old
            elif operation == 'div':
                new = old // old
        div = new // 3
        if div % check_el == 0:
            monkeys[true_monkey].append(div)
        else:
            monkeys[false_monkey].append(div)
        check_level_dict[mo_list] += 1
    monkey_li = monkeys[mo_list].copy()
    for old in monkey_li:
        monkeys[mo_list].remove(old)

# inspection(mo_list, true_monkey, false_monkey, operation, check_el, check_level_dict, operation_el=None)
for i in range(20):
    inspection('mo_0', 'mo_7', 'mo_4', 'mul', 2, check_levels, 11)
    inspection('mo_1', 'mo_3', 'mo_6', 'add', 13, check_levels, 1)
    inspection('mo_2', 'mo_1', 'mo_6', 'add', 3, check_levels, 6)
    inspection('mo_3', 'mo_7', 'mo_0', 'mul', 17, check_levels)
    inspection('mo_4', 'mo_5', 'mo_2', 'mul', 19, check_levels, 7)
    inspection('mo_5', 'mo_2', 'mo_1', 'add', 7, check_levels, 8)
    inspection('mo_6', 'mo_3', 'mo_0', 'add', 11, check_levels, 5)
    inspection('mo_7', 'mo_4', 'mo_5', 'add', 5, check_levels, 7)

print(monkeys)
print(check_levels)
