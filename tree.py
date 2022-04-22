class TreeNode:
    def __init__(self, cargo = None, left = None, right = None):
        self.cargo = cargo
        self.left = left
        self.right = right
        
    def __str__(self):
        return '('+str(self.cargo)+')'
    
class BinarySearchTree:
    def __init__(self, root = None):
        self.root = root
        
    def __str__(self):
        level = [self.root]
        
        while len(level) > 0:
            
            level_next = []
            
            for node in level:

                print('/')
                print(node, " ", end = "")
                
                if node.left is not None:
                    level_next.append(node.left) 
                if node.right is not None:
                    level_next.append(node.right)
                    
            print('\n')
            level = level_next
    
    def validate_tree(self):
        on  = self.root
        lst = []
        prev = None
        
        while len(lst) > 0 or on != None:
            while on != None:
                lst.append(on)
                on = on.left
            
            on = lst.pop()
           
            if prev != None and on.cargo <= prev.cargo: 
                return(False)

            prev = on
            on = on.right
        return(True)
    
    def check_for_cargo(self,cargo:int):
        on = self.root
        while on != None:
            if cargo > on.cargo:
                on = on.right
            elif cargo < on.cargo:
                on = on.left
            else: #condition where cargo value is equal to node.cargo
                return("cargo value Exists in the tree")
        return (False) #node.next points to None thus stopping the while loop
    
class Node:
    def __init__(self,cargo=None, next=None):
        self.cargo = cargo
        self.next = next
    
    def __str__(self):
        return "("+str(self.cargo)+")"
    
class LinkedList:
    def __init__(self,head=None):
        self.head = head
        self.length = 0
    
    def __str__(self):
        if self.head is not None:
                
            string = ''
            on = self.head
            
            while on is not None:
                string += on.__str__() + ' --> '
                on = on.next
            else:
                string += on.__str__()
            
            return string
        else:
            return 'empty list'
    
    def add_to_head(self,item_to_add):
        on = self.head
        new_item = Node(item_to_add)
        
        new_item.next = on
        self.head = new_item
        self.length += 1
        
    def add_to_tail(self, item_to_add):
        on = self.head
        if on == None:
            self.head = Node(item_to_add)
        else:
            while on.next != None: #if next node.cargo is none stay on current node
                on = on.next
            on.next = Node(item_to_add)
    
    def pop_by_index(self,index_val): #doesnt work for first index 0 and last index positions
        if self.length <= index_val:
            return("error index out of range")
        else:
            on = self.head
            while index_val != 0:
                prev = on
                on = on.next
                index_val -= 1 #distance to desired node decreases each loop

            extracted_cargo = on.cargo
            prev.next = on.next
            on.cargo = None
            on.next = None
            self.length -= 1
            return(extracted_cargo)
    
    def add_at_index(self,index_val:int,cargo):
        '''add to the tail of the desired index'''
        on = self.head
        if self.length <= index_val:
            return('Index out of Range')
        while index_val != 0:
            on = on.next
            index_val -= 1
        bumped = on.next
        on.next = Node(cargo)
        on.next.next = bumped
        self.length += 1
        
my_lst = LinkedList()
my_lst.add_to_head(1)
my_lst.add_to_head(3)
my_lst.add_to_head(6)
my_lst.add_to_tail('hi')
my_lst.add_to_tail('1i')
my_lst.add_at_index(0,"added")
print(my_lst)


            
        
        
        
            
            
            
    
        
        