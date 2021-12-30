from linked_list import Node, LinkedList
from blossom_lib import flower_definitions


class HashMap:
    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for i in range(size)]

    def hash(self, key):
        return sum(key.encode())

    def compress(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        payload = Node([key, value])
        list_at_array = self.array[array_index]
        for item in list_at_array:
            if key == item[0]:
                item[1] = value
                return
        list_at_array.insert(payload)

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        list_at_index = self.array[array_index]
        for item in list_at_index:
            if key == item[0]:
                return item[1]
        return None
        # payload = self.array[array_index]
        # if payload[0] == key:
        #   return payloa[1]
        # if payload is None or payload[0] != key:
        #   return None


blossom = HashMap(len(flower_definitions))
for element in flower_definitions:
    blossom.assign(element[0], element[1])

print(blossom.retrieve('daisy'))
print(blossom.retrieve('morning glory'))
