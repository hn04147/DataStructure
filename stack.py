class stack:

    def __init__(self, max_length):
        self.items = []
        self.max_length = max_length
        self.top = 0

    def push(self, data):
        if self.is_full() == 1:
            raise Exception("스택이 꽉 찼습니다")

        self.items.append(data)
        self.top += 1

    def is_full(self):
        if self.top == self.max_length:
            return 1
        else: return 0

    def is_empty(self):
        if self.top == 0:
            return 1
        else: return 0

    def pop(self):
        if self.is_empty() == 1:
            raise Exception("스택이 비었습니다")

        self.top -= 1
        data = self.items[self.top]
        del self.items[self.top]

        return data
    
    def display(self):
        for index in range(self.top):
            print(self.items[index], end=" ")
        print("")

def print_menu():
    print("")
    print("1. Push")
    print("2. Pop")
    print("3. print stack")
    print("4. quit")
    print("")

def main():
    new_stack = stack(50)
    while True:
        print_menu()
        index = int(input("input number: "))
        if index == 1:
            num = int(input("Input number will be pushed: "))
            new_stack.push(num)
        if index == 2:
            new_stack.pop()
        if index == 3:
            new_stack.display()
        if index == 4:
            break
        
new_stack = stack(50)
print("stack.push(123)")
new_stack.push(123)
print("stack.push(352)")
new_stack.push(352)
print("stack.push(1425)")
new_stack.push(1425)
print("stack.push(87)")
new_stack.push(87)
print("print stack: ", end="")
new_stack.display()
print("stack.pop()")
new_stack.pop()
print("stack.pop()")
new_stack.pop()
print("print stack: ", end="")
new_stack.display()
print("")

main()
