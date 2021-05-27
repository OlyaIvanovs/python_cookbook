from itertools import groupby
from operator import itemgetter
from collections import Counter
from collections import deque
import heapq

# Debug
import logging
logging.basicConfig(filename='log_filename.txt', level=logging.DEBUG,
                    format='%(asctime)s - %(message)s')


def search(lines, pattern, history=5):
    """Keeping the Last N Items"""
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


def use_search():
    with open('text.txt') as f:
        for line, prevlines in search(f, 'Python', 5):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-'*20)


class PriorityQueue:
    """implement a simple priority queue"""

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self) -> str:
        return f'Item {self.name}'


def use_priority_queue():
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)
    print([heapq.heappop(q._queue) for i in range(len(q._queue))])


def find_min_dict():
    """Calculating with Dictionaries"""
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }
    result = min(zip(prices.values(), prices.keys()))
    return result


def common_in_dicts():
    """Finding Commonalities in Two Dictionaries"""
    a = {
        'x': 1,
        'y': 2,
        'z': 3
    }

    b = {
        'w': 10,
        'x': 11,
        'y': 2
    }

    common_keys = a.keys() & b.keys()
    diff_keys = a.keys() - b.keys()
    common_values = a.items() & b.items()
    return common_keys, diff_keys, common_values


WORDS = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]


def my_top_three_items():
    """Determining the Most Frequently Occurring Items in a Sequence"""
    items = {}
    for word in WORDS:
        items[word] = items.get(word, 0) + 1
    top_three = sorted(zip(items.values(), items.keys()))[-3:]
    return top_three


def top_three_items():
    word_counts = Counter(WORDS)
    top_three = word_counts.most_common(3)
    return top_three


def sort_dicts():
    """Sorting a List of Dictionaries by a Common Key"""
    rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}]
    rows_by_fname = sorted(rows, key=itemgetter('fname'))
    return rows_by_fname


def group_records():
    """Grouping Records Together Based on a Field"""
    rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
    ]
    # Iterate over the data in chunks grouped by date

    # Sort by the desired field first
    rows.sort(key=itemgetter('date'))

    # Iterate in groups
    for date, items in groupby(rows, key=itemgetter('date')):
        print(date)
        for i in items:
            print('  ', i)


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    prices = {
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }

    p1 = {key: value for key, value in prices.items() if value > 200}
