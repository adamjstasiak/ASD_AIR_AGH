from copy import deepcopy


class Node:
    def __init__(self, value, next_value):
        self.value = value
        self.next_value = next_value

    def data(self):
        return self.value

    def next(self):
        return self.next_value


class Linked_List:
    def __init__(self):
        self.head = None

    def destroy(self):
        self.head = None

    def add(self, parameter):
        previous_val = self.head
        self.head = Node(parameter, previous_val)

    def remove(self):
        self.head = self.head.next_value

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def lenght(self):
        l = 0
        acc = self.head
        while acc is not None:
            l += 1
            acc = acc.next_value
        return l

    def get(self):
        return self.head.data()

    def print(self):
        if self.head is None:
            return
        acc = self.head
        while acc is not None:
            print(acc.data())
            acc = acc.next_value

    def add_last(self, parameter):
        if self.head is None:
            self.head = Node(parameter, None)
        else:
            acc = self.head
            while acc.next_value is not None:
                acc = acc.next_value
            acc.next_value = Node(parameter, None)

    def remove_last(self):
        if self.head.next_value is None:
            return
        prev = self.head
        for i in range(self.lenght()-2):
            prev = prev.next_value
        prev.next_value = None

    def take(self, n):
        if not isinstance(n,int):
            raise ValueError("Wrong type of parameter")
        taked_list = Linked_List()
        acc = self.head
        for i in range(n):
            taked_list.add_last(acc.data())
            acc = acc.next_value
            if acc is None:
                break
        return taked_list

    def drop(self, n):
        if not isinstance(n,int):
            raise ValueError("Wrong type of pparamater")
        drop_list = deepcopy(self)
        acc = self.head
        for i in range(n):
            drop_list.remove()
            acc = acc.next_value
            if acc is None:
                break
        return drop_list


def main():
    Uni = Linked_List()
    Uni.add(('UP', 'Poznań', 1919))
    Uni.add(('UW', 'Warszawa', 1915))
    Uni.add(('PW', 'Warszawa', 1915))
    Uni.add(('UJ', 'Kraków', 1364))
    Uni.add(('AGH', 'Kraków', 1919))
    Uni.add_last(('PG', 'Gdańsk', 1945))
    print("Pełna lista")
    Uni.print()
    print("Pierwszy Element")
    print(Uni.get())
    print("długość listy")
    print(Uni.lenght())
    A = Uni.take(4)
    B = Uni.drop(3)
    print("Pierwsze cztery elementy listy")
    A.print()
    print("Lista bez pierwszych 3 elementów")
    B.print()
    print("Usunięcie AGH")
    Uni.remove()
    Uni.print()
    print("Usunięcie PG")
    Uni.remove_last()
    Uni.print()
    Uni.destroy()
    print(Uni.is_empty())


if __name__ == "__main__":
    main()
