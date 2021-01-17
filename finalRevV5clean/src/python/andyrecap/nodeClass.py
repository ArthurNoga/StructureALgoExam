class Node:

    def __init__(self, prev: 'Node', value, next: 'Node'):
        self.__prev = prev
        self.__value = value
        self.__next = next

    def get_next(self) -> 'Node':
        return self.__next

    def set_next(self, next: 'Node') -> 'Node':
        self.__next = next
        return self

    def get_prev(self) -> 'Node':
        return self.__prev

    def set_prev(self, prev: 'Node') -> 'Node':
        self.__prev = prev
        return self

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value
        return self

    def have_next(self) -> bool:
        return self.__next is not None

    def have_prev(self) -> bool:
        return self.__prev is not None

    def __str__(self):
        return str(self.__value)

    def __eq__(self, other):
        return other == self.__value
