import random
from timeit import default_timer as timer
class Node:
    def __init__(self,priority,data):
        self.data = data
        self.priority = priority

    def __lt__(self,other):
        if self.priority < other.priority:
            return True
        else:
            return False

    def __gt__(self,other):
        if self.priority > other.priority:
            return True
        else:
            return False
    def __ge__(self,other):
        if self.priority >= other.priority:
            return True
        else:
            return False

    def __str__(self):
        return str(self.priority) + ':' + str(self.data)


class Priority_Queue:
    def __init__(self,tab=None):
        if tab is None:
            self.tab = []
            self.size = len(self.tab)
        else:
            temporary_tab = []
            for i in tab:
                if isinstance(i,tuple):
                    temporary_tab.append(Node(i[0],i[1]))
                else:
                    temporary_tab.append(Node(i,0))
            self.tab = temporary_tab
            self.size = len(self.tab)
            self.heapify()
             

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
    def heapify(self):
        for i in range(self.size//2-1,-1,-1):
            self.shift_down(i)

    def sort_heap(self):
        if self.is_empty():
            return None
        else:
            node_to_remove = self.tab[0]
            self.tab[0] = self.tab[self.size-1]
            self.tab[self.size-1] = node_to_remove
            self.size -= 1
            self.shift_down(0)


    def print_tab(self):
        print('{', end=' ')
        if len(self.tab) > 0:
            for i in range(len(self.tab) - 1):
                print(self.tab[i] , end=', ')
            if self.tab[len(self.tab) - 1]: print(self.tab[len(self.tab) - 1], end=' ')
        print('}')



    def print_tree(self, idx, lvl):
        if idx is None:
            return
        if idx<self.size:           
            self.print_tree(self.right(idx), lvl+1)
            print(2*lvl*'  ', self.tab[idx] if self.tab[idx] else None)           
            self.print_tree(self.left(idx), lvl+1)




def test1():
    tab = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    tab_to_sort = Priority_Queue(tab)
    tab_to_sort.print_tree(0,0)
    tab_to_sort.print_tab()
    tab_to_sort.heapify()
    while tab_to_sort.size > 1:
        tab_to_sort.sort_heap()
    tab_to_sort.print_tab()

def test2():
    rand_tab = [random.randint(0, 99) for _ in range(10000)]
    t_start = timer()
    rand_tab_to_sort = Priority_Queue(rand_tab)
    while rand_tab_to_sort.size > 1:
        rand_tab_to_sort.dequeue()
    t_stop = timer()
    print("Czas obliczeń:", "{:.7f}".format(t_stop - t_start),'\n')

def main():
    test1()
    test2()
if __name__ =="__main__":
    main()