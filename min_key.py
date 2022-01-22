def min_value():
    numbers = {
        "number_1": '10.5',
        "number_2": 20,
        "number_3": 3.5
    }
    values = [float(val) for val in numbers.values()]
    numbers['number_1'] = values[0]
    numbers['number_2'] = values[1]
    numbers['number_3'] = values[2]
    return "Minimum value: {} --- {}".format(min(numbers, key=numbers.get), numbers[min(numbers, key=numbers.get)])


print(min_value())