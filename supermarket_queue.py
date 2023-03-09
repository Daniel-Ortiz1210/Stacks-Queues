class Person:
    def __init__(self, name):
        self.name = name
        self.next = None


class SuperMarketQueue:
    def __init__(self, name):
        new_person = Person(name)
        self.first = new_person
        self.last = new_person
        self.length = 1

    
    def print_queue(self):
        first = self.first
        while first:
            print(first.name)
            first = first.next


    def add_to_last(self, name):

        person = Person(name)
        first_person = self.first

        if self.length == 0:
            self.first = new_person
            self.last = new_person
        else:

            while first_person.next is not None:
                first_person = first_person.next

            first_person.next = person
            self.last = person

        self.length += 1

        return person

    
    def pay_and_go(self):
        temp = self.first

        if self.length == 0:
            return None
        
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None

        self.length -= 1

        return temp



super_market_queue = SuperMarketQueue(name="Ana")
super_market_queue.add_to_last(name="Roger")
super_market_queue.add_to_last(name="Chris")

super_market_queue.pay_and_go() 

super_market_queue.print_queue()

            
