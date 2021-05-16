strings = ['a', 'b', 'c', 'd']

class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self):
        lastItem = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return lastItem

    def delete(self, index):
        #[1,2,3,4]
        # Item = self.data[index]
        if index == self.length-1:
            del self.data[index]
            self.length -=1
        self.shiftindex(index)

    def shiftindex(self, index):
        for i in range(index, self.length-1):
            print("inside", index, self.length)
            self.data[i] = self.data[i+1]
            del self.data[self.length-1]
            self.length -= 1



arr = MyArray()
arr.push(1)
arr.push(2)
arr.push(3)
arr.delete(1)
print(arr.data)
arr.delete(1)
arr.delete(10)
# arr.pop()
print(arr.data)
