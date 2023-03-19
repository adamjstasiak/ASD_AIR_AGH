#skończone
import copy
import random
from timeit import default_timer as timer

class SelectSort:
    def __init__(self,tab) -> None:
        self.tab = tab
        self.size = len(self.tab)
        

    def select_sort_swap(self):

        for i in range(self.size):
            min_el = i 
            for j in range(i,self.size):
                if self.tab[j] < self.tab[min_el]:
                    min_el = j
                    self.tab[i],self.tab[min_el] = self.tab[min_el],self.tab[i]
        return self.tab

    def select_sort_shift(self):
        i = 1 
        while i < self.size:
            j = i
            while j > 0 and self.tab[j-1] > self.tab[j]:
                self.tab[j],self.tab[j-1] = self.tab[j-1],self.tab[j]
                j -=1
            i += 1
        return self.tab



def test3():
    tab = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    tab = SelectSort(tab)
    swapped = tab.select_sort_swap()
    tab = [(5,'A'), (5,'B'), (7,'C'), (2,'D'), (5,'E'), (1,'F'), (7,'G'), (5,'H'), (1,'I'), (2,'J')]
    tab = SelectSort(tab)
    shifted = tab.select_sort_shift()
    print('Swapped: ',swapped)
    print('Shifted: ',shifted)

def test_4():
    rand_tab = [random.randint(0, 99) for _ in range(10000)]
    rand_tab_1 = copy.deepcopy(rand_tab)
    rand_tab = SelectSort(rand_tab)
    t_start_swap = timer()
    rand_tab.select_sort_swap()
    t_stop_swap = timer()
    rand_tab_1 = SelectSort(rand_tab_1)
    t_start_shift= timer()
    rand_tab.select_sort_shift()
    t_stop_shift = timer()

    print("Czas obliczeń:", "{:.7f}".format(t_stop_swap - t_start_swap))
    print("Czas obliczeń:", "{:.7f}".format(t_stop_shift - t_start_shift))

def main():
    test3()
    test_4()
if __name__ =="__main__":
    main()