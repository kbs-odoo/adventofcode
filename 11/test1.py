import sys
import numpy as np

monkeys = {'mo_0': [79, 98], 'mo_1': [54, 65, 75, 74],'mo_2': [79, 60, 97], 'mo_3': [74]}
check_levels = {'mo_0': 0, 'mo_1': 0,'mo_2': 0, 'mo_3': 0}


def inspection(mo_list, true_monkey, false_monkey, operation, check_el, check_level_dict, operation_el=None):
    for old in iter(monkeys[mo_list]):
        if operation_el:
            if operation == 'mul':
                new = np.multiply(old, operation_el)
            elif operation == 'sub':
                new = np.substract(old, operation_el)
            elif operation == 'add':
                new = np.add(old, operation_el)
            elif operation == 'div':
                new = np.floor_divide(old, operation_el)
        else:
            if operation == 'mul':
                new = np.multiply(old, old)
            elif operation == 'sub':
                new = np.substract(old, old)
            elif operation == 'add':
                new = np.add(old, old)
            elif operation == 'div':
                new = np.floor_divide(old, old)
        div = np.floor_divide(new, 3)
        if np.mod(div, check_el) == 0:
            monkeys[true_monkey].append(div)
        else:
            monkeys[false_monkey].append(div)
        check_level_dict[mo_list] += 1
    monkeys[mo_list] = []

# inspection(mo_list, true_monkey, false_monkey, operation, check_el, check_level_dict, operation_el=None)
for i in iter(range(20)):
    inspection('mo_0', 'mo_2', 'mo_3', 'mul', 23, check_levels, 19)
    inspection('mo_1', 'mo_2', 'mo_0', 'add', 19, check_levels, 6)
    inspection('mo_2', 'mo_1', 'mo_3', 'mul', 13, check_levels)
    inspection('mo_3', 'mo_0', 'mo_1', 'add', 17, check_levels, 3)

print(monkeys)
print(check_levels)
