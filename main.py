#Polygon
import math
class Polygon:
    def __init__(self,e,r):
        self.edge = e
        self.radius = r

    def interior_angle(self):
        return (self.edge - 2)*180/(self.edge)

    def edge_length(self):
        return 2*self.radius*math.sin(math.pi/self.edge)

    def apothem(self):
        return self.radius * math.cos(math.pi / self.edge)

    def area(self):
        return 0.5*self.edge*self.edge_length()*self.apothem()

    def perimeter(self):
        self.edge * self.edge_length()

    def __repr__(self):
        return f'Polygon with edge={self.edge} and radius={self.radius}'

    def __eq__(self,other):
        return (self.edge == other.edge) and (self.radius == other.radius)

    def __gt__(self,other):
        return (self.edge > other.edge)

a = Polygon(6,5)
print(f'the polygon is {a}')

print(f'interior angle is {a.interior_angle()}')

print(f'edge length is {a.edge_length()}')

print(f'apothem is {a.apothem()}')

print(f'area is {a.area()}')

print(f'perimeter is {a.perimeter()}')

b = Polygon(6,5)

print(f'equality of a and b is {a == b}')

c = Polygon(2,5)

print(f'is a bigger than c :{a > c}')
