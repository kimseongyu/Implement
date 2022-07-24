class bitmaksing:
    def __init__(self):
        self.bit = 0

    def add(self, n):
        self.bit = self.bit | (1<<n)

    def remove(self, n):
        self.bit = self.bit & ~(1<<n)

    def toggle(self, n):
        self.bit = self.bit ^ (1<<n)

    def full(self, n):
        self.bit = (1<<(n+1)) - 1

    def empty(self):
        self.bit = 0

    def check(self, n):
        return (self.bit>>n) & 1

    def size(self):
        size = 0
        set = self.bit >> 1
        while set:
            if set % 2 == 1:
                size += 1
            set = set >> 1
        return size

    def subSet(self):
        list = []
        set = self.bit >> 1
        subset = self.bit >> 1
        while subset:
            list.append(bin(subset))
            subset = (subset-1)&set
        return list

    # 실행될 함수의 인자는 부분집합
    def subSetIterator(self, func):
        set = self.bit >> 1
        subset = self.bit >> 1
        while subset:
            func(subset)
            subset = (subset-1)&set