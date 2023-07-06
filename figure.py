class Circle:
    def __init__(self, radius: int):
        self._radius = radius

    def get_radius(self):
        print(f"Радиус: {self._radius}")
        return self._radius

    def calculate_area_circle(self):
        print(f"Площадь: {3.14 * self._radius * self._radius}")
        return 3.14 * self._radius * self._radius

    def perimeter_circle(self):
        print(f"Периметр: {3.14 * 2 * self._radius}")
        return 3.14 * 2 * self._radius


class Rectangle:
    def __init__(self, a: int, b: int):
        self._a = a
        self._b = b

    def get_sides(self):
        print(f"Стороны: {self._a}, {self._b}")
        return self._a, self._b

    def calculate_area(self):
        print(f"Площадь: {self._a*self._b}")
        return self._a*self._b

    def perimeter(self):
        print(f"Периметр: {(self._a + self._b) * 2}")
        return (self._a + self._b) * 2


class Square(Rectangle):
    def __init__(self, a: int):
        super().__init__(a, a)


def main():
    circle = Circle(3)
    print(circle.get_radius(), circle.calculate_area_circle(), circle.perimeter_circle())
    rectangle = Rectangle(2, 3)
    print(rectangle.get_sides(), rectangle.calculate_area(), rectangle.perimeter())
    square = Square(5)
    print(square.get_sides(), square.calculate_area(), square.perimeter())


if __name__ == '__main__':
    main()




