from trees import Node


def count_univals(root: Node):
    if root.left is None and root.right is None:
        return 1
    total_univals = 0
    if root.left is not None and root.right is not None:
        total_univals += (root.left.val == root.right.val)
    if root.left is not None:
        total_univals += count_univals(root.left)
    if root.right is not None:
        total_univals += count_univals(root.right)
    return total_univals


if __name__ == '__main__':
    node = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))
    print(f'There are {count_univals(node)} univals in the node')
    assert count_univals(node) == 5



