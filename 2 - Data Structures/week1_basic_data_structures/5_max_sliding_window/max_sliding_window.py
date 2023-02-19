# python3

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__stack_ordered = []
        self.length = 0
    
    def Push(self, a):
        self.__stack.append(a)
        self.length += 1
        if len(self.__stack_ordered) == 0:
            self.__stack_ordered.append(a)
        else:
            if a >= self.__stack_ordered[-1]:
                self.__stack_ordered.append(a)
            else:
                self.__stack_ordered.append(self.__stack_ordered[-1])
    
    def Pop(self):
        if len(self.__stack) == 0:
            return None
        self.length -= 1
        self.__stack_ordered.pop()
        return self.__stack.pop()

    def Max(self):
        if len(self.__stack_ordered) == 0:
            return None
        return self.__stack_ordered[-1]

def max_sliding_window_naive(sequence, m):
    maximums = []
    stack1 = StackWithMax()
    stack2 = []

    for i in range(m):
        stack1.Push(sequence[i])
   
    maximums.append(stack1.Max())

    for i in range(m, len(sequence)):
        # every operation here takes O(1)
        while stack1.length > 0:
            stack2.append(stack1.Pop())
        stack2.pop()
        while len(stack2) > 0:
            stack1.Push(stack2.pop())
        stack1.Push(sequence[i])
        
        maximums.append(stack1.Max())

    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window_naive(input_sequence, window_size))

