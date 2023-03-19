class Node:
    def __init__(self,data,priority):
        self.data = data
        self.priority = priority

    def __it__(self,other):
        if self.priority < other.priority:
            return True
        else:
            return False

    def __gt__(self,other):
        if self.priority > other.priority:
            return True
        else:
            return False

    def __str__(self):
        return str(self.priority) + ':' + str(self.data)


class Priority_Queue:
    def __init__(self):
        self.tab = []
        self.size = 0

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False


    def left(self,key)->int:
        if 2*key +1 < self.size:
            return 2*key+1
        else:
            return None


    def right(self,key)->int:
        if 2*key+2 < self.size:
            return 2*key+2
        else:
            return None

    def parent(self,key)->int:
        if key > 0:
            return (key-1)//2
        else: 
            return None


    def peek(self):
        if self.size == 0:
            return None
        else:
            return self.tab[0].data


    def shift_up(self,index):
        bufor = self.tab[self.parent(index)]
        while index > 0 and self.tab[self.parent(index)] < self.tab[index] :
            self.tab[self.parent(index)] = self.tab[index]
            self.tab[index] = bufor
            index = self.parent(index)

    def enqueue(self,prio,value):
        new_node = Node(value,prio)
        if self.size == 0:
            self.tab.append(new_node)
            self.size = 1
            return
        else:
            self.tab.append(new_node)
            index = self.size
            self.size +=1
            self.shift_up(index)

    def shift_down(self,index):
        while self.left(index) is not None and self.right(index) is not None:
            if self.tab[self.left(index)] < self.tab[index] and self.tab[self.right(index)] < self.tab[index]:
                break
            if self.tab[self.left(index)] > self.tab[self.right(index)]:
                bufor = self.tab[self.left(index)]
                self.tab[self.left(index)] = self.tab[index]
                self.tab[index] = bufor
                index = self.left(index)
            else:
                bufor = self.tab[self.right(index)]
                self.tab[self.right(index)] = self.tab[index]
                self.tab[index] = bufor
                index = self.right(index)

        
    def dequeue(self):
        if self.size == 0:
            return None
        else:
            node_to_remove = self.tab[0]
            self.tab[0] = self.tab[self.size-1]
            self.tab[self.size-1] = node_to_remove
            self.size -= 1
            self.tab.pop()
            self.shift_down(0)
            return node_to_remove.data

    def print_tab(self):
        print ('{', end=' ')
        if self.size == 0:
            print('}')
        else:
            for i in range(self.size-1):
                print(self.tab[i], end = ', ')
            if self.tab[self.size-1]: print(self.tab[self.size-1] , end = ' ')
            print( '}')


    def print_tree(self, idx, lvl):
        if idx is None:
            return
        if idx<self.size:           
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)           
            self.print_tree(self.left(idx), lvl+1)


def main():
    heap = Priority_Queue()
    keys = [4, 7, 6, 7, 5, 2, 2, 1]
    values = ["A","L","G","O","R","Y","T","M"]
    for i in range(len(keys)):
            heap.enqueue(keys[i],values[i])
    heap.print_tree(0,0)
    heap.print_tab()
    print(heap.dequeue())
    print(heap.peek())
    heap.print_tab()
    while heap.size != 0:
        print(heap.dequeue())
    print(heap.is_empty())
    heap.print_tab()
if __name__ =="__main__":
    main()
