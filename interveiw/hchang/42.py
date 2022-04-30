from Structure import TreeNode
# 이진트리의 최대 깊이를 구하여라
from collections import deque
null = None
a = [3,9,20,null,null,15,7]

root = TreeNode(a)
root.print_all()


count = 0
nodes = deque([(root,count)])

while nodes:
    node, count = nodes.popleft()
    if node: nodes.extend([(node.left,count+1),(node.right,count+1)])

print(count)