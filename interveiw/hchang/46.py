from Structure import TreeNode
null = None
a = TreeNode([1,3,2,5,3,4,4,3,2,4,2,2])
#      1 
#   3    2
# 5
b = TreeNode([2,null,3,null,null,null,7])

#         2
#             3
#                7

def merge(t1, t2):
    if t1 and t2:
        node = TreeNode(t1.val + t2.val)
        node.left = merge(t1.left, t2.left)
        node.right = merge(t1.right, t2.right)
        
        return node 
    else:
        return t1 or t2 

a.print_all(num=50)
print(b)
print(merge(a,b))
