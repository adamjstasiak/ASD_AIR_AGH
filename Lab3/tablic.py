
class Queue:
    def __init__(self,size_tab=5):
        self.size_tab = size_tab
        self.que = [None for i in range(size_tab)]
        self.begin = 0 # odczyt
        self.end = 0   # zapisz

    def realloc(self):
        old_size = len(self.que)
        self.end = self.size_tab
        self.size_tab *= 2
        return [self.que[i] if i<old_size else None  for i in range(self.size_tab)]

    def is_empty(self):
        if self.begin == self.end:
            return True
        else:
            return False

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.que[self.begin]

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            holder = self.que[self.begin]
            self.begin = (self.begin +1) % self.size_tab
            return holder


    def enqueue(self,data):
        self.que[self.end]=data
        self.end = (self.end+1) % self.size_tab
        if self.end == self.begin:
            self.que = self.realloc()
            holder_tab = self.que[self.begin:int(self.size_tab/2)]
            for i in range(self.begin,int(self.size_tab/2)):
                self.que[i] = None
                for j in range(1,self.end):
                    self.que[-j] = holder_tab[-j]
            indexes = [self.begin,self.end]
            self.begin = indexes[0] + indexes[1]
            self.end = indexes[0]
    
    def TablePrint(self):
        if self.begin == self.end:
            print("[]")
        else:
            print("[",end="")
            for i in range(self.size_tab):
                print(self.que[i],end=",")
            print("]")
    def QueuePrint(self):
        if self.begin == self.end:
            print("[]")
        elif self.begin < self.end:
            print("[",end="")
            for i in range(self.begin,self.end):
                print(self.que[i],end=",")
            print("]")
        else:
            print("[",end="")
            for i in range(self.begin,self.size_tab):
                print(self.que[i],end=",")
            for i in range(0,self.end):
                print(self.que[i],end=",")
            print("]")


def main():
    Q = Queue()
    Q.TablePrint()
    Q.QueuePrint()
    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)
    Q.enqueue(4)
    print(Q.dequeue())
    print(Q.peek())
    Q.TablePrint()
    Q.QueuePrint()
    Q.enqueue(5)
    Q.enqueue(6)
    Q.enqueue(7)
    Q.enqueue(8)
    Q.TablePrint()
    Q.QueuePrint()
    while not Q.is_empty():
        Q.dequeue()
    Q.TablePrint()
    Q.QueuePrint()
if __name__ =="__main__":
    main()

