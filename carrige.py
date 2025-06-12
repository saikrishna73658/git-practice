class Carrier:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


carrier = Carrier()
carrier.push('Rice Box')
carrier.push('Curry Box')
carrier.push('Curd Box')
print(carrier.items)
print('peek method result ---',carrier.peek()) 
print(carrier.items)
print('pop method result ---',carrier.pop())  
print(carrier.items)  
print('size method result ---',carrier.size())
print('is_empty method result ---',carrier.is_empty())

