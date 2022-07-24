class ArrayList:

    __capacity = __size = __element = 0

    def __init__(self, givenCapacity = 100):
        self.__capacity = givenCapacity

    def setCapacity(self, newCapacity):
        self.__capacity = newCapacity

    def __setSize(self, newSize):
        self.__size = newSize

    def setElements(self, newElements):
        self.__element = newElements

    def capacity(self):
        return self.__capacity

    def size(self):
        return self.__size

    def element(self):
        return self.__element

a = ArrayList()
print(a)