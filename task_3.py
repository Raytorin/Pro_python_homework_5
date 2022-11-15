from task_3_logger import logger


@logger
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_lists = list_of_list

    def __iter__(self):
        self.cursor = 0
        self.i = 0
        return self

    def __next__(self):
        count_len = len(self.list_of_lists)
        if self.i == len(self.list_of_lists[self.cursor]):
            self.i = 0
            self.cursor += 1
            if self.cursor > (count_len - 1):
                raise StopIteration
        item = self.list_of_lists[self.cursor][self.i]
        self.i += 1
        return item


list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

FlatIterator(list_of_lists_1)
