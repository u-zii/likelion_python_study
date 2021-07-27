class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        Shape.__init__(self)
        self.length=length

    def area(self):
        return self.length**2

a=int(input("정사각형의 한 변의 길이를 입력하세요 : "))
b=Square(a)
print("정사각형의 넓이는", b.area(), "입니다.")