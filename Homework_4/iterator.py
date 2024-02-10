class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.index = 0
        self.subindex = 0
        return self

    def __next__(self):
        if self.index < len(self.list_of_list):
            element = self.list_of_list[self.index]
            if self.subindex < len(element):
                sub_element = element[self.subindex]
                self.subindex += 1
                return sub_element
            else:
                self.index += 1
                self.subindex = 0
                return next(self)

        else:
            raise StopIteration


def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == [
        'a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None
        ]


if __name__ == '__main__':
    test_1()
