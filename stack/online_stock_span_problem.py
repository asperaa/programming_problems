"""Online stock span problem"""
class StockSpan:
    def __init__(self):
            self.price_stack = []
            self.count_stack = []
    
    def next(self, price):
        less_than_count = 1
        if not self.price_stack:
            self.price_stack.append(price)
            self.count_stack.append(less_than_count)
            return self.count_stack[-1]
        while self.price_stack and self.price_stack[-1] <= price:
            less_than_count += self.count_stack.pop()
            self.price_stack.pop()
        self.count_stack.append(less_than_count)
        self.price_stack.append(price)
        return self.count_stack[-1]

if __name__ == "__main__":
    ss = StockSpan()
    print(ss.next(31))
    print(ss.next(41))
    print(ss.next(48))
    print(ss.next(59))
    print(ss.next(79))
    # print(ss.next(75))
    # print(ss.next(85))

        
