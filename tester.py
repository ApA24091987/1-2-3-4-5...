def calculate_structure_sum(data_structure):
    total_sum = 0

    def recursive_sum(data):
        nonlocal total_sum
        if isinstance(data, (int, float)):
            total_sum += data
        elif isinstance(data, str):
            total_sum += len(data)
        elif isinstance(data, (list, tuple, set)):
            for item in data:
                recursive_sum(item)
        elif isinstance(data, dict):
            for key, value in data.items():
                recursive_sum(key)
                recursive_sum(value)

    recursive_sum(data_structure)
    return total_sum

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)