class Figure:
    unit = 'см'

    def __init__(self, color, car):
        self.car = car
        self.color = color


    def calculate_area(self):
        pass

    def info(self):
        pass


class Circle(Figure):
    def __init__(self, radius, color):
        super(Circle, self).__init__(color)
        self.__radius = radius


    def get_radius(self):
        return self.__radius

    def set_radius(self, value):
        self.__radius = value

    def calculate_area(self):
        return (3.14 * self.__radius ** 2)

    def info(self):
        return f'Circle radius :{self.__radius}' \
               f'area : {self.calculate_area()}{self.unit}'


circle = Circle(2)
print(circle.info())


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        super(RightTriangle, self).__init__()
        self.__side_a = side_a
        self.__side_b = side_b

    def get_side_a(self):
        return self.__side_a

    def set_side_a(self, new_side_a):
        self.__side_a = new_side_a

    def get_side_b(self):
        return self.__side_b

    def set_side_b(self, new_side_b):
        self.__side_b = new_side_b

    def calculate_area(self):
        return (1 / 2 * self.__side_b * self.__side_a)

    def info(self):
        return f'Right triangle side a : {self.__side_a}{self.unit}' \
               f'side b :{self.__side_b}{self.unit}' \
               f'area :{self.calculate_area()}{self.unit}'


triangle = RightTriangle(3, 4)
print(triangle.info())


def create_figures():
    circle1 = Circle(5)
    circle2 = Circle(3)
    circle3 = Circle(7)
    triangle1 = RightTriangle(3,6)
    triangle2 = RightTriangle(4,7)

    lst1 = [circle1, circle2, circle3, triangle1, triangle2]
    return lst1


lst1 = create_figures()

for i in lst1:
  print(i.info())





