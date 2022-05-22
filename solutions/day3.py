from trees import *

def serialize(root: Node):
    serialized = str(len(root.val))+root.val
    serialized += 'l' if root.left is not None else '_'
    serialized += 'r' if root.right is not None else '_'
    serialized += "("
    if root.left is not None:
        serialized += serialize(root.left)
    serialized += ")"
    serialized += "("
    if root.right is not None:
        serialized += serialize(root.right)
    serialized += ")"

    return serialized


def deserialize(serialized_string: str):
    length_of_val = int(serialized_string[0])
    val = serialized_string[1:1+length_of_val]
    has_left_child = (serialized_string[1+length_of_val] == 'l')
    has_right_child = (serialized_string[2 + length_of_val] == 'r')
    left_child, right_child = None, None
    brackets_seen = 0
    left_end_index = 0
    for i in range(1, len(serialized_string)):
        if serialized_string[i] == "(":
            brackets_seen += 1
        elif serialized_string[i] == ")":
            brackets_seen -= 1
            if brackets_seen == 0:
                left_end_index = i
                break
    if has_left_child:
        left_child = deserialize(serialized_string[4+length_of_val:left_end_index])
    if has_right_child:
        right_child = deserialize(serialized_string[left_end_index+2:-1])

    return Node(val, left_child, right_child)


if __name__ == '__main__':
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
