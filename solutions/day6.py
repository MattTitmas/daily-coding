from random import randint

memory = dict()

class LinkedListNode:
    def __init__(self, val):
        self.__val = val
        self.__pointer = randint(1000,1000000)
        self.__xor = 0
        while self.__pointer in memory.keys():
            self.__pointer = randint(1000, 1000000)
        memory[self.__pointer] = self

    @property
    def get_val(self):
        return self.__val

    @property
    def get_pointer(self):
        return self.__pointer

    @property
    def get_xor(self):
        return self.__xor

    def set_xor(self, new_val):
        self.__xor = new_val

class XORLinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, val):
        new_node = LinkedListNode(val)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            prev = 0
            while current_node.get_xor ^ prev != 0:
                old_node = current_node
                current_node = memory[current_node.get_xor ^ prev]
                prev = old_node.get_pointer
            current_node.set_xor(prev ^ new_node.get_pointer)
            new_node.set_xor(current_node.get_pointer)

    def get(self, index):
        current_node = self.head
        memory_location = current_node.get_pointer
        prev = 0

        while index > 0:
            old_node = current_node
            memory_location = current_node.get_xor ^ prev
            current_node = memory[current_node.get_xor ^ prev]
            prev = old_node.get_pointer
            index -= 1
        return memory[memory_location].get_val


if __name__ == '__main__':
    XORList = XORLinkedList()
    XORList.add_node(5)
    XORList.add_node(3)
    XORList.add_node(1)
    XORList.add_node(5)
    XORList.add_node(3)
    XORList.add_node(1)

    print(XORList.get(0))
    print(XORList.get(1))
    print(XORList.get(2))
    print(XORList.get(3))
    print(XORList.get(4))
    print(XORList.get(5))


