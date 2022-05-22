class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @property
    def get_string_val(self):
        return str(self.val)

    def __str__(self, tab=0):
        to_ret = ''
        if self.right != None:
            to_ret += self.right.__str__(tab=tab + 1)
        to_ret += '\t' * tab + '-> ' + self.get_string_val + '\n'
        if self.left != None:
            to_ret += self.left.__str__(tab=tab + 1)
        return to_ret
