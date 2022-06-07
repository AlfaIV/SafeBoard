class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
  
  
class Stack:
  
    # Initializing a stack.
    # Use a dummy node, which is
    # easier for handling edge cases.
    def __init__(self):
        self.head = Node("head")
        self.size = 0
  
    # String representation of the stack
    def __str__(self):
        cur = self.head.next
        out = ""
        while cur:
            out += str(cur.value) + "->"
            cur = cur.next
        return out[:-3]
  
    # Get the current size of the stack
    def getSize(self):
        return self.size
  
    # Check if the stack is empty
    def isEmpty(self):
        return self.size == 0
  
    # Get the top item of the stack
    def peek(self):
  
        # Sanitary check to see if we
        # are peeking an empty stack.
        if self.isEmpty():
            raise Exception("Peeking from an empty stack")
        return self.head.next.value
  
    # Push a value into the stack.
    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1
  
    # Remove a value from the stack and return.
    def pop(self):
        if self.isEmpty():
            raise Exception("Popping from an empty stack")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return remove.value
        
class main:
    
    def __init__(self):
        self.support_char = ["(",")","[","]","<",">","{","}"]
    
    def Check(self,Input_list_of_element):
        stack = Stack()
        for i in range(len(Input_list_of_element)):
            #print("*",Input_list_of_element[i])
            if Input_list_of_element[i] in self.support_char[::2]:
                stack.push(Input_list_of_element[i])
                pointer = i
            if Input_list_of_element[i] in self.support_char[1::2]:
                remove = stack.pop()
                #print(remove)
                remove = self.support_char[self.support_char.index(remove) + 1]
                #print(remove)
                if remove != Input_list_of_element[i]:
                    return i + 1
        if stack.isEmpty() == True:
            return True
        else:
            return pointer + 1
            
    def Test(self):
        try:
            if self.Check([i for i in "[qwerty;]"]) != True:
                print("Fail Test 1",self.Check([i for i in "[qwerty;]"]))
                raise()
            if self.Check([i for i in "a[a(i]"]) != 6:
                print("Fail Test 2",self.Check([i for i in "a[a(i]"]))
                raise()
            if self.Check([i for i in "{{{tttt"]) != 3:
                print("Fail Test 3",self.Check([i for i in "{{{tttt"]))
                raise()
        except:
            print('Ошибка')
        else:
            print('Всё хорошо.')
            

if __name__ == "__main__":
    support_char = ["(",")","[","]","<",">","{","}"]
    main_prog = main()
    print(main_prog.Check([i for i in input()]))
    #main_prog.Test()
    #print(main_prog.Check([i for i in "[qwerty;]"]))
    #input_char = [i for i in input() if i in support_char]
    #Check(support_char)
    #Test()

