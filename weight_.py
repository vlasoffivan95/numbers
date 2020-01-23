import random
import json
BIAS = 7  # пороговое значение
delta_weight = 0.8  # шаг приращения весов

numbers_code = [
    '111101101101111',  # 0
    '001001001001001',  # 1
    '111001111100111',  # 2
    '111001111001111',  # 3
    '101101111001001',  # 4
    '111100111001111',  # 5
    '111100111101111',  # 6
    '111001001001001',  # 7
    '111101111101111',  # 8
    '111101111001111'  # 9
]

numbers_weight = {}


def get_weights_number(target, bias):
    weights = [0] * 15
    for k in range(100000):
        i = random.randint(0, 9)  # выбираем цифру
        s = sum([int(i1) * i2 for i1, i2 in zip(list(numbers_code[i]), weights)])
        is_recognize = (s >= bias)
        if i == target and not is_recognize:
            for j in range(15):
                if numbers_code[i][j] == '1':
                    weights[j] += delta_weight  # поощрение
        if i != target and is_recognize:
            for j in range(15):
                if numbers_code[i][j] == '1':
                    weights[j] -= delta_weight  # наказание

    numbers_weight[target] = weights

# расчет весов для цифр 1...9
for i in range(10):
    get_weights_number(i, 7)

# запись в json-файл
with open('weights.json', 'w') as f:
    f.write(json.dumps(numbers_weight, sort_keys=True, indent=4))


