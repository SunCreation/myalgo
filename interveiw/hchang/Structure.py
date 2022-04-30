from collections import deque
class TreeNode:
    def __init__(self,data=None,left=None,right=None):
        self.left = left
        self.right = right
        if type(data)==list:
            self.val = data[0]
            nextnode = deque([self.add_left, self.add_right])
            for i in data[1:]:
                addnode = nextnode.popleft()
                node = addnode(i)
                nextnode.extend([node.add_left, node.add_right])
            self.cutNoneNode()
        else: self.val = data
    def __repr__(self):
        self.print_all()
        return ''

    def to_list(self):
        result = [self.val]
        q = deque([self.left,self.right])
        while q:
            node = q.popleft()
            if node:
                result.append(node.val)
                q.extend([node.left,node.right])
            else: result.append(None)
        while result[-1] is None:
            result.pop()
        return result

    def add_left(self,data):
        self.left = TreeNode(data)
        return self.left

    def add_right(self,data):
        self.right = TreeNode(data)
        return self.right

    def print_all(self,num=60):
        self.addNoneNode()
        count = 0
        nodelist = self.to_list()
        while 2**count < len(nodelist)+1:
            if count:
                for i in nodelist[2**count-1:2**(count+1)-1]:
                    if i is None: i = ''
                    print(' '*(num//(2**count+1)-len(str(i))),i, end='')
                print()
            else: print(' '*(num//2),nodelist[0])
            count+=1
        self.cutNoneNode()

    def cutNoneNode(self):
        node = self
        if node.left:
            if node.left.val is None: node.left = None
            else: node.left.cutNoneNode()
        if node.right:
            if node.right.val is None: node.right = None
            else: node.right.cutNoneNode()

    def addNoneNode(self):
        if self.left or self.right:
            if not self.left: self.left = TreeNode(None)
            if not self.right: self.right = TreeNode(None)
            self.left.addNoneNode()
            self.right.addNoneNode()