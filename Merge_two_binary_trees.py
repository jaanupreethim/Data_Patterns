class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(nodes):
    if not nodes or nodes[0] == 'N':
        return None
    root = TreeNode(int(nodes[0]))
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        curr = queue.pop(0)
        if i < len(nodes) and nodes[i] != 'N':
            curr.left = TreeNode(int(nodes[i]))
            queue.append(curr.left)
        i += 1
        if i < len(nodes) and nodes[i] != 'N':
            curr.right = TreeNode(int(nodes[i]))
            queue.append(curr.right)
        i += 1
    return root

def serialize_tree(root):
    if not root:
        return "Empty"
    res, queue = [], [root]
    while queue:
        curr = queue.pop(0)
        if curr:
            res.append(str(curr.val))
            queue.append(curr.left)
            queue.append(curr.right)
        else:
            res.append("N")
    while res and res[-1] == "N":
        res.pop()
    return " ".join(res)

def merge_trees(t1, t2):
    if not t1 and not t2:
        return None
    if not t1:
        return t2
    if not t2:
        return t1
    merged = TreeNode(t1.val + t2.val)
    merged.left = merge_trees(t1.left, t2.left)
    merged.right = merge_trees(t1.right, t2.right)
    return merged

if __name__ == "__main__":
    t1_input = input("Enter Tree 1 space-separated level-order (e.g. 1 3 2): ").split()
    t2_input = input("Enter Tree 2 space-separated level-order (e.g. 2 1 3): ").split()
    tree1 = build_tree(t1_input)
    tree2 = build_tree(t2_input)
    merged_tree = merge_trees(tree1, tree2)
    print("Merged Tree:", serialize_tree(merged_tree))
