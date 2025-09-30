# BST
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L---")
        if self.right:
            ret += self.right.__str__(level + 1, "R---")
        return ret
    
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)

def delete(root, key):
    if not root:
        return root

    if key < root.val:
        root.left = delete(root.left, key)
    elif key > root.val:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        elif not root.right:
            temp = root.left
            root = None
            return temp
        root.val = min_value_node(root.right)
        root.right = delete(root.right, root.val)
    return root

def min_value_node(root):
    if not root:
        return None
    current = root
    while current.left:
        current = current.left
    return current.val

def max_value_node(root):
    if not root:
        return None
    current = root
    while current.right:
        current = current.right
    return current.val

def total_node_values_recursive(root):
    if not root:
        return 0
    return root.val + total_node_values_recursive(root.left) + total_node_values_recursive(root.right)

def total_node_values_iter(root):
    if not root:
        return 0
    sum = 0
    temp = [root]
    while temp:
        node = temp.pop()
        sum += node.val
        if node.left:
            temp.append(node.left)
        if node.right:
            temp.append(node.right)
    return sum

# Test
root = Node(7)
for key in [3, 2, 9, 17, 20, 81, 4, 12]:
    root = insert(root, key)

print("Tree structure:")
print(root)

print("Min value:", min_value_node(root))
print("Max value:", max_value_node(root))
print("Sum of all values (recursive):", total_node_values_recursive(root))
print("Sum of all values (iterative):", total_node_values_iter(root))


