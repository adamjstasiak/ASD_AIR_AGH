
class Node:
    def __init__(self,key,value,left,right):
        self.key = key 
        self.value = value
        self.left = left
        self.right = right
        
class Root:
    def __init__(self,head = None):
        self.head = head

    def search(self, key):
        return self._search(key, self.head)


    def _search(self, key, node):
        if node is None:
            return None
        elif key == node.key:
            return node.value
        elif key < node.key:
            return self._search(key, node.left)
        elif key > node.key:
            return self._search(key, node.right)


    def insert(self, key, value):
        if self.head is None:
            self.head = Node(key,value,None,None)
            return
        else:    
            return self._insert(key, value, self.head)

   
    def _insert(self, key, value, node):
        if node is None:
            node = Node(key, value, None, None)
            return node
        elif key == node.key:
            node.value = value
            return node
        elif key < node.key:
            node.left = self._insert(key, value, node.left)
            return node
        elif key > node.key:
            node.right = self._insert(key, value, node.right)
            return node

            
    def delete(self, key):
        if self.head is None:
            return 
        return self._delete(key, self.head, None)

    
    def _delete(self, key, current_node, parent_node):
        if current_node is None:
            return None
        elif key == current_node.key:
            return self._cut_node(parent_node, current_node)
        elif key < current_node.key:
            return self._delete(key, current_node.left, current_node)
        elif key > current_node.key:
            return self._delete(key, current_node.right, current_node)
        
    def _cut_node(self, parent_node, current_node):
        if current_node.left is None and current_node.right is None:
            self._cut_node_with_no_children(parent_node, current_node)
        elif bool(current_node.left is None) ^ bool(current_node.right is None):
            self._cut_node_with_one_child(parent_node, current_node)
        else:
            self._cut_node_with_two_children(parent_node, current_node)
        return current_node.value

            
    def _cut_node_with_no_children(self, parent_node, current_node):
        if parent_node is None:
            self.head = None
        elif parent_node.left.key == current_node.key:
            parent_node.left = None
        else:
            parent_node.right = None
            

    def _cut_node_with_one_child(self, parent_node, current_node):
        node_to_pin = None
        if current_node.left is not None:
            node_to_pin = current_node.left
            current_node.left = None
        else:
            node_to_pin = current_node.right
            current_node.right = None

        if parent_node is None:
            self.head = node_to_pin
        elif parent_node.left.key == current_node.key:
            parent_node.left = node_to_pin
        else:
            parent_node.right = node_to_pin
        
    def _cut_node_with_two_children(self, parent_node, current_node):
        node_to_pin_l = current_node.left
        node_to_pin_r = current_node.right
        if parent_node is None:
            self.head = node_to_pin_r
        elif parent_node.left.key == current_node.key:
            parent_node.left = node_to_pin_r
        else:
            parent_node.right = node_to_pin_r
        min_node_in_subtree = self._get_node_with_min_value_in_subtree(node_to_pin_r)
        min_node_in_subtree.left = node_to_pin_l
        
    def _get_node_with_min_value_in_subtree(self, node):
        current_node = node
        while current_node.left is not None:
            current_node = current_node.left
        return current_node


    def height(self):
        return self._height(self.head)
    
    def _height(self,node):
        if node is None:
            return 0
        else:
            return 1 + max(self._height(node.left), self._height(node.right))

    def print_tree(self):
        print("==============")
        self._print_tree(self.head, 0)
        print("==============")

    def _print_tree(self, node, lvl):
        if node!=None:
            self._print_tree(node.right, lvl+5)

            print()
            print(lvl*" ", node.key, node.value)
     
            self._print_tree(node.left, lvl+5)

    def tree_in_to_list(self):
        print("[", end="")
        self._tree_in_to_list(self.head)
        print("]")
    def _tree_in_to_list(self,node):
        if node is not None:
            self._tree_in_to_list(node.left)
            print(" {0}: {1} ".format(node.key,node.value), end="")
            self._tree_in_to_list(node.right)






def main():
    B = Root()
    l = {50:'A', 15:'B', 62:'C', 5:'D', 20:'E', 58:'F', 91:'G', 3:'H', 8:'I', 37:'J', 60:'K', 24:'L'}
    for i in l:
        B.insert(i , l[i])
    B.print_tree()
    B.tree_in_to_list()
    print(B.height())
    print(B.search(24))
    B.insert(20,'AA')
    B.insert(6,'M')
    B.delete(62)
    B.insert(59,'N')
    B.insert(100,'P')
    B.delete(8)
    B.delete(15)
    B.insert(55,"R")
    B.delete(50)
    B.delete(5)
    B.delete(24)
    print(B.height())

    B.tree_in_to_list()
    B.print_tree()

if __name__ == '__main__':
    main()
