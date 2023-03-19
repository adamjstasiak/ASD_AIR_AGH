
class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        
    
class hash_table:
    def __init__(self,size,c1=1,c2=0):
        self.size = size
        self.table = [None for i in range(size)]
        self.c1 = c1
        self.c2 = c2



    def hash_metod(self,key):
        if isinstance(key,str):
            sum = 0 
            for char in key:
                sum += ord(char)
            mod = sum % self.size
        else: 
            mod = key % self.size
        return mod
        

    def quad_probing(self,key,i):
        return (self.hash_metod(key) + self.c1 * i + self.c2 * (i**2)) % self.size

    def search(self,key):
        for data in self.table:
            if data is not None:
                if data.key == key:
                    return data.value
        return None            
        
        

    def insert(self,key,data):
        current_data = self.table[self.hash_metod(key)]
        if current_data is None:
            self.table[self.hash_metod(key)] = Node(key,data)
        elif key == current_data.key:
            self.table[self.hash_metod(key)] = Node(key,data)
        else:
            i = 1
            while i <= self.size:
                if self.table[self.quad_probing(key,i)] is None:
                    self.table[self.quad_probing(key,i)] = Node(key,data)
                    return
                i+=1    
            print("Brak miejsca")
            return
            
            
            

    def remove(self,key):
        if self.table[self.hash_metod(key)] is None:
            print("Brak danej")
            return
        else:
            self.table[self.hash_metod(key)] = None
 
    
    def __str__(self):
        string = '{'
        for i in self.table:
            if i != None:
                string += (str(i.key) + ': '  + str(i.value)+ ' ') 
            else:
                string += (str(i) + ': ' + str(None) + ' ')
        string += '}' 
        return string

def test1(size,c1=1,c2=0):
    t = hash_table(size,c1,c2)
    t.insert(1,'A')
    t.insert(2,'B')
    t.insert(3,'C')
    t.insert(4,'D')
    t.insert(5,'E')
    t.insert(18,'F')
    t.insert(31,'G')
    t.insert(8,'H')
    t.insert(9,'I')
    t.insert(10,'J')
    t.insert(11,'K')
    t.insert(12,'L')
    t.insert(13,'M')
    t.insert(14,'N')
    t.insert(15,'O')
    print(t)
    print("Value of key number 5:", end=" ")
    print(t.search(5))
    print("Value of key number 14:", end=" ")
    print(t.search(14))
    print("Overwriting key number 5 with Z", end=" ")
    t.insert(5,"Z")
    print(t.search(5))
    print("Removing value of key number 5")
    t.remove(5)
    print(t)
    print("Value of key number 31:",end="")
    print(t.search(31))
    print("inserting value W with key test")
    t.insert("test","W")
    print(t)
def test2(size,c1,c2):
    letter = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O" ]
    t = hash_table(size,c1,c2)
    for i in range(len(letter)):
        t.insert(13*i,letter[i])
    print(t)

    



def main():
    print("test numer 1")
    test1(13)
    print("test numer 2")
    test2(13,1,0)
    print("test numer 2 próbkowanie kwadratowe")
    test2(15,0,1)
    print("test numer 1 próbkowanie kwadratowe")
    test1(13,0,1)
if __name__ =="__main__":
    main()
