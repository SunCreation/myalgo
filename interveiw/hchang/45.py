from Structure import TreeNode

root = TreeNode([4,2,7,1,3,6,9,3,5,6,2,1,6,7,2,2,7,3,8,3,2,2,8])

root.print_all()

def swap(self):
    self.left, self.right = self.right, self.left
    if self.left: self.left.swap()
    if self.right: self.right.swap()

TreeNode.swap = swap
root.swap()

root.print_all()