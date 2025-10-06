from dataclasses import dataclass
from typing import TypeVar

r"""
- node_list: Simple binary tree
      5
    /   \
   3     8
  / \   / \
 1  4  7   9
      /
     6
"""
node_list1: list[int | None] = [
    5,
    3,
    8,
    1,
    4,
    7,
    9,
    None,
    None,
    None,
    None,
    6,
    None,
    None,
    None,
]


r"""
- node_list2: Binary search tree
     10
   /    \
  5      15
 / \    /  \
3   7  12  18
"""
node_list2: list[int] = [10, 5, 15, 3, 7, 12, 18]


T = TypeVar("T")


@dataclass
class TreeNode[T]:
    value: T
    left: "None | TreeNode" = None
    right: "None | TreeNode" = None

    def __str__(self):
        return f"TreeNode(value={self.value},left={self.left},right={self.right})"


def list_to_tree(nodes: list[T] | list[T | None], index: int = 0) -> TreeNode[T] | None:
    if index >= len(nodes):
        return None

    if nodes[index] is None:
        return None

    node = nodes[index]
    assert node
    root: TreeNode[T] = TreeNode(node, None, None)

    root.left = list_to_tree(nodes, 2 * index + 1)
    root.right = list_to_tree(nodes, 2 * index + 2)

    return root


tree1 = list_to_tree(node_list1)
tree2 = list_to_tree(node_list2)


def depth(root: TreeNode | None) -> int:
    if root is None:
        return 0

    depth_l = depth(root.left) + 1
    depth_r = depth(root.right) + 1

    return max(depth_l, depth_r)


print("## Depth")
assert depth(tree1) == 4
assert depth(tree2) == 3


def in_order(node: TreeNode[T] | None, result: list[T]) -> list[T]:
    if node is None:
        return result

    in_order(node.left, result)
    result.append(node.value)
    in_order(node.right, result)

    return result


print("## In-Order")
assert in_order(tree1, []) == [1, 3, 4, 5, 6, 7, 8, 9]
assert in_order(tree2, []) == [3, 5, 7, 10, 12, 15, 18]  # Sorted!


def pre_order(node: TreeNode[T] | None, result: list[T]) -> list[T]:
    if node is None:
        return result

    result.append(node.value)
    pre_order(node.left, result)
    pre_order(node.right, result)

    return result


print("## Pre-Order")
assert pre_order(tree1, []) == [5, 3, 1, 4, 8, 7, 6, 9]
assert pre_order(tree2, []) == [10, 5, 3, 7, 15, 12, 18]


def post_order(node: TreeNode[T] | None, result: list[T]) -> list[T]:
    if node is None:
        return result

    post_order(node.left, result)
    post_order(node.right, result)
    result.append(node.value)

    return result


print("## Pre-Order")
assert post_order(tree1, []) == [1, 4, 3, 6, 7, 9, 8, 5]
assert post_order(tree2, []) == [3, 7, 5, 12, 18, 15, 10]
