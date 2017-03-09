class ListObject:
    def __init__(self):
        self.local_list = []

    def add_to_list(self, value):
        self.local_list.append(value)

    def sum_in_list(self):
        return sum(self.local_list)


list_1 = ListObject()
list_2 = ListObject()

list_1.add_to_list(2)
list_1.add_to_list(2)
list_1.add_to_list(2)

list_2.add_to_list(5)
list_2.add_to_list(5)

print(list_1.sum_in_list())
print(list_2.sum_in_list())
