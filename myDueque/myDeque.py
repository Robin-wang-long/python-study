# 在这里完成例6-2的程序调试
class myDeque:
    def __init__(self, iterable=None, maxlen=10):
        if iterable == None:
            self._content = []
            self._current = []
        else:
            self._content = list(iterable)
            self._current = len(iterable)
        self._size = maxlen
        if self._size < self._current:
            self._size = self._current

    def __del__(self):
        del self._content

    def setSize(self, size):
        if size < self._current:
            for i in range(size, self._current)[::-1]:
                del self._content[i]
            self._current = size
        self._size = size

    def appendRight(self, v):
        if self._current < self._size:
            self._content.append(v)
            self._current = self._current + 1
        else:
            print('The queue if full')

    def appendLeft(self, v):
        if self._current < self._size:
            self._content.insert(0, v)
            self._current = self._current + 1
        else:
            print("The queue is full")

    def popLeft(self):
        if self._content:
            self._current = self._current - 1
            return self._content.pop(0)
        else:
            print("The queue is empty")

    def popRight(self):
        if self._content:
            self._current = self._current - 1
            return self._content.pop()
        else:
            print("The queue is empty")

    def rotate(self, k):
        if abs(k) > self._current:
            print('k must<=' + str(self._current))
            return
        self._content = self._content[-k:] + self._content[:-k]

    def reverse(self):
        self._content = self._content[::-1]

    def __len__(self):
        return self._current

    def __str__(self):
        return 'myDeque(' + str(self._content) + ',maxlen=' + str(self._size) + ')'

    __repr__ = __str__

    def clear(self):
        self._current = []
        self._current = 0

    def isEmpty(self):
        return not self._content

    def isFull(self):
        return self._current == self._size


if __name__ == '__main__':
    print('please use me as a module.')