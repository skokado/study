from typing import TypeVar, Optional

from dataclasses import dataclass

T = TypeVar("T")


@dataclass
class Node[T]:
    value: T
    prev: Optional["Node"] = None
    next: Optional["Node"] = None

    def __str__(self) -> str:
        return f"Node({self.value})"


@dataclass
class DoublyLinkedList[T]:
    head: Node[T] | None
    tail: Node[T] | None

    def is_empty(self) -> bool:
        return self.head is None

    def push(self, data: T):
        new_node = Node(data)

        # empty case
        if not (self.head and self.tail):
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def lpush(self, data: T):
        new_node = Node(data)

        # empty case
        if not (self.head and self.tail):
            self.head = new_node
            self.tail = new_node
            return

        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node

    def index(self, i: int) -> Node[T]:
        count = 0
        current = self.head
        while current and count < i:
            current = current.next
            count += 1

        if current is None:
            raise IndexError("out of size")

        return current

    def pop(self, i: int | None = None) -> Node[T]:
        if i is None:
            if self.tail is None:
                raise IndexError("list is empty")

            new_tail = self.tail.prev
            if new_tail:
                new_tail.next = None
            return self.tail

        node = self.index(i)

        if not (node.prev or node.next):
            self.head = None
            self.tail = None
            return node

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        return node

    def __str__(self) -> str:
        if (current := self.head) is None:
            return ""

        result = str(current)
        while current.next:
            result += " <---> " + str(current.next)
            current = current.next

        return result


if __name__ == "__main__":
    node = Node(0)
    dll = DoublyLinkedList(node, node)

    dll.push(1)
    dll.push(2)
    dll.push(3)
    assert str(dll) == "Node(0) <---> Node(1) <---> Node(2) <---> Node(3)"
    assert str(dll.index(0)) == "Node(0)"
    assert str(dll.index(3)) == "Node(3)"
    try:
        dll.index(4)
    except IndexError:
        # OK
        pass

    dll.lpush(4)
    assert str(dll) == "Node(4) <---> Node(0) <---> Node(1) <---> Node(2) <---> Node(3)"

    assert str(dll.pop()) == "Node(3)"
    assert str(dll) == "Node(4) <---> Node(0) <---> Node(1) <---> Node(2)"

    assert str(dll.pop(2)) == "Node(1)"
    assert str(dll) == "Node(4) <---> Node(0) <---> Node(2)"

    print("OK.")
