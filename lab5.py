from abc import ABC, abstractmethod
from math import sqrt
from shapely.geometry import Polygon
from shapely import area as p_area, length as p_length


# исключения
class FigureExceptions(Exception):
    def __init__(self, message='Ошибка в координатах фигуры'):
        self.message = message

    def __str__(self):
        return self.message


class TriangleExceptions(Exception):
    def __init__(self, message='Несуществующий треугольник'):
        self.message = message

    def __str__(self):
        return self.message


class QuadExceptions(Exception):
    def __init__(self, message='Несуществующий четырехугольник'):
        self.message = message

    def __str__(self):
        return self.message


# асбтрактный класс - фигура
class Figure(ABC):
    @property
    @abstractmethod
    def area(self):
        pass

    @property
    @abstractmethod
    def perimeter(self):
        pass


# класс - треугольник
class Triangle(Figure):
    def __init__(self, coords):
        self.coords = coords
        self.__a, self.__b, self.__c = 0, 0, 0  # будут переопределены позже

        self.__isValidTriangle()
        print('Треугольник с координатами', *coords)

    def __isValidTriangle(self):
        if len(self.coords) != 3 or not (all(x >= 0 and y >= 0 for (x, y) in self.coords)):
            raise FigureExceptions
        else:
            x1, y1 = self.coords[0][0], self.coords[0][1]
            x2, y2 = self.coords[1][0], self.coords[1][1]
            x3, y3 = self.coords[2][0], self.coords[2][1]
            a = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            b = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
            c = sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
            if not (a + b > c and a + c > b and b + c > a):
                raise TriangleExceptions
            else:
                self.__a, self.__b, self.__c = a, b, c

    @property
    def area(self):  # формула Герона
        p = self.perimeter / 2
        area = sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))
        return round(area, 3)

    @property
    def perimeter(self):
        return self.__a + self.__b + self.__c

    def isNotScalene(self):  # если стороны не равны между собой - треугольник разносторонний
        if self.__a != self.__b and self.__b != self.__c and self.__c != self.__a:
            return False
        else:
            return True

    def trianglesOverlap(self, other):  # метод из библиотеки shapely
        t1 = Polygon(self.coords)
        t2 = Polygon(other.coords)
        return t1.intersects(t2)


# класс - четырехугольник
class Quadrilateral(Figure):
    def __init__(self, coords):
        self.coords = coords

        self.isValidQuad()
        print('Четырехугольник с координатами', *coords)

    def isValidQuad(self):
        if len(self.coords) != 4 or not (all(x >= 0 and y >= 0 for (x, y) in self.coords)):
            raise FigureExceptions
        elif len(set(self.coords)) != 4:
            raise QuadExceptions
        else:
            quad = Polygon(self.coords)
            if not quad.is_valid:
                raise QuadExceptions

    @property
    def area(self):  # метод из библиотеки shapely
        quad = Polygon(self.coords)
        return round(p_area(quad), 3)

    @property
    def perimeter(self):  # метод из библиотеки shapely
        quad = Polygon(self.coords)
        return round(p_length(quad), 3)

    def isNotIrregular(self):
        # если противоположные стороны равны друг другу - четырехугольник параллелограм
        # прямоугольник и ромб - частные случаи паралеллограма, поэтому этой проверки достаточно
        x1, y1 = self.coords[0][0], self.coords[0][1]
        x2, y2 = self.coords[1][0], self.coords[1][1]
        x3, y3 = self.coords[2][0], self.coords[2][1]
        x4, y4 = self.coords[3][0], self.coords[3][1]
        a = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        b = sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
        c = sqrt((x4 - x3) ** 2 + (y4 - y3) ** 2)
        d = sqrt((x4 - x1) ** 2 + (y4 - y1) ** 2)
        if a == c and d == b:
            return True
        else:
            return False


# fail_triangle = Triangle([(0, 0), (1, 1)])
# fail_triangle = Triangle([(0, 0), (0, 0), (0, 10)])
# fail_triangle = Triangle([(0, 0), (1, 1), (2, 2)])

# fail_quad = Quadrilateral([(0, 0), (0, 9,), (0, 10)])
# fail_quad = Quadrilateral([(0, 0), (0, 0), (4, 4), (2, 0)])
# fail_quad = Quadrilateral([(1, 1), (2, 2), (3, 3), (4, 4)])

tr1 = Triangle([(0, 0), (0, 4), (6, 7)])
print('Площадь: {0}\nЯвляется равносторонним/равнобедренным: {1}'.format(tr1.area, tr1.isNotScalene()), end='\n\n')

tr2 = Triangle([(0, 0), (4, 0), (2, 8)])
print('Площадь: {0}\nЯвляется равносторонним/равнобедренным: {1}'.format(tr2.area, tr2.isNotScalene()))
print('Пересечение с треугольником {0[0]} {0[1]} {0[2]}: {1}'.format(tr1.coords, tr2.trianglesOverlap(tr1)), end='\n\n')

tr3 = Triangle([(10, 0), (10, 10), (15, 5)])
print('Площадь: {0}\nЯвляется равносторонним/равнобедренным: {1}'.format(tr3.area, tr3.isNotScalene()))
print('Пересечение с треугольником {0[0]} {0[1]} {0[2]}: {1}'.format(tr1.coords, tr3.trianglesOverlap(tr1)), end='\n\n')

qu1 = Quadrilateral([(0, 0), (1, 2), (5, 7), (3, 1)])
print('Площадь: {0}\nЯвляется паралелограммом: {1}'.format(qu1.area, qu1.isNotIrregular()), end='\n\n')

qu2 = Quadrilateral([(0, 0), (1, 1), (2, 1), (1, 0)])
print('Площадь: {0}\nЯвляется паралелограммом: {1}'.format(qu2.area, qu2.isNotIrregular()), end='\n\n')

qu3 = Quadrilateral([(0, 0), (0, 5), (5, 5), (5, 0)])
print('Площадь: {0}\nЯвляется паралелограммом: {1}'.format(qu3.area, qu3.isNotIrregular()), end='\n\n')
