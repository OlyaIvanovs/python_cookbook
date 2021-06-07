"""Effective Python: 90 Specific Ways to write Better Python."""
from types import prepare_class


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x*x for x in a if x % 2 == 0]
# print(squares)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [x for row in matrix for x in row]
# print(flat)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_gt_4 = [x for x in a if x % 2 == 0 and x > 4]
# print(even_gt_4)


stock = {
    'nails': 125,
    'screws': 35,
    'wingnuts': 8,
    'washers': 24,
}

order = ['screws', 'wingnuts', 'clips']


def get_batches(count, size):
    return count // size


result = {}
for name in order:
    count = stock.get(name, 0)
    batches = get_batches(count, 8)

    if batches:
        result[name] = batches

# print(result)

found = {name: get_batches(stock.get(name, 0), 8)
         for name in order if get_batches(stock.get(name, 0), 8)}
# print(found)

found = ((name, batches)
         for name in order if (batches := get_batches(stock.get(name, 0), 8)))
# print(next(found))
# print(next(found))


half = [(last := count // 2) for count in stock.values()]
# print(f'Last item of {half} is {last}')


def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result


def normalize(numbers):
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


def normalize_copy(numbers):
    numbers_copy = list(numbers)
    total = sum(numbers_copy)
    result = []
    for value in numbers_copy:
        percent = 100 * value / total
        result.append(percent)
    return result


def normalize_func(get_iter):
    total = sum(get_iter())  # New iterator
    result = []
    for value in get_iter():  # New iterator
        percent = 100 * value / total
        result.append(percent)
    return result


def read_visits(file_path):
    with open(file_path) as f:
        for line in f:
            yield int(line)


it = read_visits('my_numbers.txt')
percentages = normalize(it)
print(percentages)

path = 'my_numbers.txt'
percentages = normalize_func(lambda: read_visits(path))
print(percentages)


def normalize_defensive(numbers):
    if iter(numbers) is numbers:
        raise TypeError
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


class ReadVisits:
    def __init__(self, data_path):
        self.data_path = data_path

    def __iter__(self):
        with open(self.data_path) as f:
            for line in f:
                yield int(line)


visits = ReadVisits(path)
percentages = normalize(visits)
print(percentages)
