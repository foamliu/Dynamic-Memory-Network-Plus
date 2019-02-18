import re

import numpy as np

if __name__ == '__main__':
    filename = 'log.txt'
    pattern = '\\[Run (\\d+), Task (\\d+), Epoch (\\d+)\\] \\[([A-Z])\\w+\\] Accuracy : (\\d+(\\.\\d+)?)'
    with open(filename, 'r') as file:
        lines = file.readlines()

    max_acc = np.zeros((20,), np.float)

    for line in lines:
        m = re.search(pattern, line)
        if m:
            run_id = int(m.group(1))
            task_id = int(m.group(2))
            epoch_id = int(m.group(3))
            set_name = str(m.group(4))
            accuracy = float(m.group(5))
            if set_name == 'T' and accuracy > max_acc[task_id - 1]:
                max_acc[task_id - 1] = accuracy

    for i in range(20):
        print('Task {} Accuracy : {}'.format(i + 1, max_acc[i]))
