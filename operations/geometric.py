from exceptions import GeometricException


class GeometricOps:
    __PI = 3.14  # Kinda Private through Name Mangling (Not truly private)

    @staticmethod
    def area_square(len: int):
        if len < 0:
            raise GeometricException("Length cannot be negative", "area_square")
        return len**2

    @staticmethod
    def area_rect(len: int, breadth: int):
        if len < 0:
            raise GeometricException("Length cannot be negative", "area_rect")
        if breadth < 0:
            raise GeometricException("Breadth cannot be negative", "area_rect")
        return len * breadth

    @staticmethod
    def area_circle(radius: int):
        if radius < 0:
            raise GeometricException("Radius cannot be negative", "area_circle")
        return GeometricOps.__PI * radius * radius

    @staticmethod
    def circumference_circle(radius: int):
        if radius < 0:
            raise GeometricException("Radius cannot be negative", "area_circle")
        return GeometricOps.__PI * 2 * radius
