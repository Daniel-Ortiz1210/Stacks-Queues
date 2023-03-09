class Book():
    def __init__(self, title, next=None):
        self.title = title
        self.next = next


class BookStack():
    def __init__(self, bottom=None, top=None):
        self.bottom = bottom
        self.top = top
    
    def push(self, book):
        if self.bottom is None:
            self.bottom = book
            self.top = self.bottom
        else:
            self.top.next = book
            self.top = book
    
    def pop(self):
        
        if self.bottom.next is None:
            self.bottom = None
            self.top = None
        else:
            current = self.bottom
            while current != None:
                if current.next.next == None:
                    current.next = None
                    self.top = current
                    break
                current = current.next

    
    def print_stack(self):
        top = self.bottom

        while top != None:
            print(top.title)
            top = top.next



book1 = Book("Math")
book2 = Book("Spanish")
book3 = Book("Science")

my_stack = BookStack()

my_stack.push(book1)
my_stack.push(book2)
my_stack.push(book3)
my_stack.pop()
my_stack.print_stack()
